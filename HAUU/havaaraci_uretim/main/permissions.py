from rest_framework.permissions import BasePermission

class Izinler(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if view.action in ['create', 'update', 'destroy']:
            takim_id = request.user.takim.id  
            return str(request.data.get('takim')) == str(takim_id)

        return True
