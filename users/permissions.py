from rest_framework.permissions import BasePermission

class IsMentor(BasePermission):
    """
    Faqatgina Mentorlar uchun ruxsat
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'mentor'
