from rest_framework import permissions

class IsCustomerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False 

        if user.role in ["ceo", "mentor"]:
            return True  

        if user.role == "admin":
            return True

        return False  

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role in ["ceo", "mentor"]:
            return True  

        if user.role == "admin":
            return obj.company == user.company

        return False  