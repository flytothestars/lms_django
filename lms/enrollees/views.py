from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from core.mixins import BasePageMixin
from courses.models import CourseSpecification
from enrollees.forms import TempEnrolleeForm
from enrollees.models import TempEnrollee


class TempEnrolleeCreate(BasePageMixin, CreateView):
    model = TempEnrollee
    form_class = TempEnrolleeForm
    success_message = _("Заявка отправлена")
    template_name = "courses/course_form.html"
    title = _("Отправка заявки")
    nav_section = "courses"
    nav_tab = "course"

    def form_valid(self, form):
        form.instance.course_schedule_id = self.request.POST.get("course_schedule_id")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_specification = CourseSpecification.objects.prefetch_related(
            "courses"
        ).get(id=self.request.GET.get("course_specification_id"))
        context["course_specification"] = course_specification
        return context

    def get_success_url(self):
        previous = self.request.GET.get("previous")
        if previous is None:
            return reverse_lazy("index")
        else:
            return previous
        
class PrintPdfDetailView(DetailView):
    model = TempEnrollee
    template_name = "admin/pdf_print_page.html"
    title = _("Распечатать отчет")


def approve_object(request, pk):
    obj = get_object_or_404(TempEnrollee, pk=pk)
    obj.status = TempEnrollee.STATUS_ACCEPTED  # Обновляем статус на "Одобрено"
    obj.save()
    message = """
    Уважаемый предприниматель,
    Благодарим за проявленный интерес к Программе обучения Almaty Business—2022.

    По контактам, указанным в Вашей заявке с Вами свяжется наш координатор.

    С уважением, Организаторы Программы
    e-mail: almatybusiness.gov@gmail.com
    Вопросы по тел +77473360439

    Құрметті кәсіпкер,
    AlmatyBusiness—2022 оқу бағдарламасына қызығушылық танытқаныңыз үшін ризашылығымызды білдіреміз.

    Өтініміңіз қабылданды және расталды.
    Біздің үйлестірушілер сіздің өтініміңізде көрсетілген байланыс нөміріне хабарласады.

    Құрметпен, Бағдарлама ұйымдастырушылары
    e-mail: almatybusiness.gov@gmail.com
    Сұрақтар мен осы тел: +77473360439
    """
    
    
    send_mail(
        'Edu Almaty Business',
        message,
        'settings.EMAIL_HOST_USER',
        [obj.email],
        fail_silently=False
    )
    return HttpResponseRedirect(reverse('admin:%s_%s_changelist' % (obj._meta.app_label, obj._meta.model_name)))

