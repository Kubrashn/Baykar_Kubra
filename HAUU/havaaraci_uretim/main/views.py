from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def uretim_paneli(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  
        ucak_id = request.GET.get('ucak_id') 
        if ucak_id:  
            ucak = get_object_or_404(Ucak, id=ucak_id)  
            required_parts = ["Kanat", "Gövde", "Kuyruk", "Aviyonik"]  
            parca_bilgisi = [] 
            for part in required_parts:  
                parca = Parca.objects.filter(ucak=ucak, parca_adi__icontains=part).first()  
                if parca:  # Parça varsa
                    eksik = parca.stok < 1  
                    parca_bilgisi.append({
                        "id": parca.id,
                        "ad": parca.parca_adi,
                        "stok": parca.stok,
                        "eksik": eksik,
                    })
                else:
                    parca_bilgisi.append({
                        "ad": part,
                        "stok": 0,
                        "eksik": True,
                    })

            return JsonResponse({"parcalar": parca_bilgisi})
    
    ucaklar = Ucak.objects.all() 
    return render(request, 'uretim_paneli.html', {'ucaklar': ucaklar})


def get_parcalar(request, ucak_id):
    takim = request.user.takim  
    parcalar = Parca.objects.filter(ucak_id=ucak_id, takim=takim)  

    parca_list = [{"id": parca.id, "ad": parca.parca_adi} for parca in parcalar]
    
    return JsonResponse({"parcalar": parca_list})


def uretim_yap(request, parca_id):
    parca = Parca.objects.get(id=parca_id) 
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Giriş yapmalısınız!"}, status=403)

    Uretim.objects.create(user=request.user, parca=parca)  

    parca.stok += 1
    parca.save() 

    return JsonResponse({"message": f"{parca.parca_adi} başarıyla üretildi!", "stok": parca.stok})


def get_montaj_parcalari(request, ucak_id):
    required_parts = ["Kanat", "Gövde", "Kuyruk", "Aviyonik"]
    parcalar = []
    for part in required_parts:
        try:
            parca = Parca.objects.get(ucak_id=ucak_id, parca_adi=part, takim=request.user.takim)
            eksik = parca.stok < 1
            parcalar.append({"id": parca.id, "ad": parca.parca_adi, "stok": parca.stok, "eksik": eksik})
        except Parca.DoesNotExist:
            parcalar.append({"ad": part, "stok": 0, "eksik": True})
    return JsonResponse({"parcalar": parcalar})


def montaj_uretim_yap(request, ucak_id):
    parcalar = Parca.objects.filter(ucak_id=ucak_id, takim=request.user.takim)

    eksik_parca = any(parca.stok < 1 for parca in parcalar)  
    if eksik_parca:
        return JsonResponse({"error": "Eksik parça bulunuyor!"}, status=400)

    for parca in parcalar:
        Uretim.objects.create(user=request.user, parca=parca) 
        parca.stok -= 1  
        parca.save()  

    return JsonResponse({"message": "Tüm montaj parçaları üretildi!"})

def get_gercek_parcalar(request, ucak_id):

    required_parts = ["Kanat", "Gövde", "Kuyruk", "Aviyonik"]
    
    parcalar = Parca.objects.filter(ucak_id=ucak_id)
    mevcut_parcalar = [parca.parca_adi for parca in parcalar]

    missing_parts = [part for part in required_parts if part not in mevcut_parcalar]
    
    return JsonResponse({"missing_parts": missing_parts})

