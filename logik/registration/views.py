from .forms import UserCreationFormWhitEmail, ProfileForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWhitEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb2', 'placeholder':'Email valido'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb2', 'placeholder':'Confirma tu contraseña'})
        return form

@method_decorator(login_required, name="dispatch")
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # Funcion para obtener el User por medio de request para que sepa cual usuario actualiza su perfil
    def get_object(self):
        # Recuperar el objeto(User) que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
