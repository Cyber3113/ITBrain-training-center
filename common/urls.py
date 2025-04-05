from rest_framework.routers import DefaultRouter
from app_admins import views as admin_views
from app_groups import views as group_views
from app_mentors import views as mentor_views
from app_students import views as student_views
from app_attendance import views as attendance_views

router = DefaultRouter()


router.register('admin', admin_views.AdminViewSet, basename='admin')
router.register('group', group_views.GroupViewSet, basename='group')
router.register('mentor', mentor_views.MentorViewSet, basename='mentor')
router.register('student', student_views.StudentViewSet, basename='student')
router.register('attendance', attendance_views.AttendanceViewSet, basename='attendance')


urlpatterns = [

              ] + router.urls
