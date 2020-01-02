from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.contrib.auth import login

from accounts.forms import SignUpForm
from .models import User


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        form = self.get_form()
        user = User.objects.get(username=form.data.get('username'))

        login(self.request, user)
        return reverse('proto1:event_list')


class AccountDetailView(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs["user_id"])

        return render(request, 'accounts/user_detail.html', {'user': user})
