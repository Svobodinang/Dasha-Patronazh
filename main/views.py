from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError

from django.http import HttpResponse, HttpResponseRedirect

from .forms import *


class MainView(FormView):
    template_name = 'main/index.html'
    form_class = MainForm
    success_url = 'thanks'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context["main_form"] = self.form_class(self.request.GET or None)
        context["main_form_mob"] = MainFormMob(self.request.GET or None)
        context["help_form"] = HelpForm(self.request.GET or None)
        context['need_help_form'] = HelpYouForm(self.request.GET or None)
        context['can_help_form'] = CanToHelpForm(self.request.GET or None)
        return context

    def post(self, request, *args, **kwargs):
        main_form = MainForm(self.request.POST)
        main_form_mob = MainFormMob(self.request.POST)
        help_form = HelpForm(self.request.POST)
        help_you_form = HelpYouForm(self.request.POST)
        can_help_form = CanToHelpForm(self.request.POST)
        if main_form.is_valid():
            name = main_form.cleaned_data['name']
            number = main_form.cleaned_data['number']
            email = main_form.cleaned_data['email']
            subject = "Заявка на обслуживание"
            message = "Имя фамилия: " + name + "\nНомер телефона: " + number + "\nE-mail: " + email
            recipients = ['admin@патронаж32.рф']
            try:
                 send_mail(subject, message, 'admin@патронаж32.рф', recipients)
            except BadHeaderError:
                return HttpResponse("Invalid header number")
            return HttpResponseRedirect(self.success_url)
        else:
            HttpResponse('Invalid header number')

        if main_form_mob.is_valid():
            name = main_form_mob.cleaned_data['name']
            number = main_form_mob.cleaned_data['number']
            email = main_form_mob.cleaned_data['email']
            subject = "Заявка на обслуживание"
            message = "Имя фамилия: " + name + "\nНомер телефона: " + number + "\nE-mail: " + email
            recipients = ['svobodinang@mail.ru']
            try:
                 send_mail(subject, message, 'svobodinang@mail.ru', recipients)
            except BadHeaderError:
                return HttpResponse("Invalid header number")
            return HttpResponseRedirect(self.success_url)
        else:
            HttpResponse('Invalid header number')

        if help_form.is_valid():
            name = help_form.cleaned_data['name']
            number = help_form.cleaned_data['number']
            email = help_form.cleaned_data['email']
            need = help_form.cleaned_data['need']
            subject = "Благотворительная помощь по заявке"
            message = "Имя фамилия: " + name + "\nНомер телефона: " + number + "\nE-mail: " + email + "\nНуждается в: " + need
            recipients = ['svobodinang@mail.ru']
            try:
                send_mail(subject, message, 'svobodinang@mail.ru', recipients)
            except BadHeaderError:
                return HttpResponse("Invalid header number")

            return HttpResponseRedirect(self.success_url)

        else:
            HttpResponse('Invalid header number')

        if help_you_form.is_valid():
            name = help_you_form.cleaned_data['name']
            number = help_you_form.cleaned_data['number']
            email = help_you_form.cleaned_data['email']
            need = help_you_form.cleaned_data['need']
            subject = "Нуждается в помощи"
            message = "Имя фамилия: " + name + "\nНомер телефона: " + number + "\nE-mail: " + email + "\nНуждается в: " + need
            recipients = ['svobodinang@mail.ru']
            try:
                send_mail(subject, message, 'svobodinang@mail.ru', recipients)
            except BadHeaderError:
                return HttpResponse("Invalid header number")

            return HttpResponseRedirect(self.success_url)

        if can_help_form.is_valid():
            name = can_help_form.cleaned_data['name']
            number = can_help_form.cleaned_data['number']
            email = can_help_form.cleaned_data['email']
            help = can_help_form.cleaned_data['need']
            subject = "Может помочь"
            message = "Имя фамилия: " + name + "\nНомер телефона: " + number + "\nE-mail: " + email + "\nНуждается в: " + help
            recipients = ['svobodinang@mail.ru']
            try:
                send_mail(subject, message, 'svobodinang@mail.ru', recipients)
            except BadHeaderError:
                return HttpResponse("Invalid header number")

            return HttpResponseRedirect(self.success_url)


class ThanksView(TemplateView):
    template_name = 'main/thanks.html'





