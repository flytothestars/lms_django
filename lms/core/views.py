from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render 

from core.mixins import BasePageMixin
from courses.models import VideoCourse, VideoCourseCategory, Course
from enrollees.models import TempEnrollee
from directory.models import Activity, AutomationSystem, ParticipationPurpose, ProblemOrTask
from teachers.models import Teacher
from enrollees.forms import TempEnrolleeForm
from django.http import JsonResponse

class IndexPage(BasePageMixin, TemplateView):
    model = TempEnrollee
    form_class = TempEnrolleeForm
    success_message = _("Заявка отправлена")
    title = _("Главная")
    template_name = "core/index.html"
    nav_section = "core"
    nav_tab = "index"
    
        
    def post(self, request, *args, **kwargs):
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        company_name = request.POST.get("company_name")
        identification_number = request.POST.get("identification_number")
        activity = request.POST.get("activity")
        description = request.POST.get("description")
        number_of_completed_years = request.POST.get("number_of_completed_years")
        employee_count = request.POST.get("employee_count")
        is_recording_customers = request.POST.get("is_recording_customers")
        is_recording_average_check = request.POST.get("is_recording_average_check")
        course_type = request.POST.get("course_type")
        automation_system = request.POST.get("automation_system")
        problem_or_task = request.POST.get("problem_or_task")
        participation_purpose = request.POST.get("participation_purpose")
        lang = request.POST.get("lang")
        promo_code = request.POST.get("promo_code")
        activity_model = Activity.objects.get(id=activity)
        automation_system_model = AutomationSystem.objects.get(id=automation_system)
        problem_or_task_model = ProblemOrTask.objects.get(id=problem_or_task)
        participation_purpose_model = ParticipationPurpose.objects.get(id=participation_purpose)
        course_type_model = Course.objects.get(id=course_type)
        enrollee = TempEnrollee(
            full_name=full_name,
            phone_number=phone_number,
            email=email,
            company_name=company_name,
            identification_number=identification_number,
            activity=activity_model,
            description=description,
            number_of_completed_years=number_of_completed_years,
            employee_count=employee_count,
            is_recording_customers=is_recording_customers,
            is_recording_average_check=is_recording_average_check,
            course_type=course_type_model,
            automation_system=automation_system_model,
            problem_or_task=problem_or_task_model,
            participation_purpose=participation_purpose_model,
            lang=lang,
            promo_code=promo_code,
        )
        enrollee.save()
        return render(request, "core/index.html")
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        teachers = Teacher.objects.prefetch_related("courses").all()
        video_course_categories = VideoCourseCategory.objects.all()
        video_courses = VideoCourse.objects.select_related(
            "video_course_category"
        ).all()
        context["teachers"] = teachers
        context["video_course_categories"] = video_course_categories
        context["video_courses"] = video_courses
        context["form"] = TempEnrolleeForm
        context["request"] = self.request
        return context
    


class AboutPage(BasePageMixin, TemplateView):
    title = _("О нас")
    template_name = "core/about.html"
    nav_section = "core"
    nav_tab = "index"

# def block(request, *args, **argv):
#     return render(request, 'core/block.html')

class ExpertPage(BasePageMixin, TemplateView):
    title = _("Эксперты")
    template_name = "core/expert.html"
    nav_section = "core"
    nav_tab = "index"


class KnowledgeBasePage(BasePageMixin, TemplateView):
    title = _("История проекта")
    template_name = "core/knowledge_base.html"
    nav_section = "core"
    nav_tab = "index"
