from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from BlogEstadiosApp.forms import LoginForm, CustomUserCreationForm, EstadioForm, UserProfileUpdateForm
from BlogEstadiosApp.models import UserProfile, Estadio
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView


def home(request):
    if request.user.is_authenticated:
        return redirect("estadios")
    else:
        return redirect("login")


def about_me(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'BlogEstadiosApp/about_me.html', {'user_profile': user_profile})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('home')
            except User.DoesNotExist:
                messages.error(request, "Credenciales inválidas.")
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()

            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.username = form.cleaned_data['username']
            user_profile.password = form.cleaned_data['password1']
            user_profile.email = form.cleaned_data['email']
            user_profile.avatar = form.cleaned_data['avatar']
            user_profile.description = form.cleaned_data['description']
            user_profile.portfolio_link = form.cleaned_data['portfolio_link']
            user_profile.save()

            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def estadios(request):
    estadios = Estadio.objects.all()
    return render(request, 'BlogEstadiosApp/estadios.html', {"estadios": estadios})


def estadio_detail(request, estadio_id):
    estadio = get_object_or_404(Estadio, pk=estadio_id)
    return render(request, 'BlogEstadiosApp/estadio_detail.html', {'estadio': estadio})


@login_required
def crear_estadio(request):
    if request.method == "POST":
        form = EstadioForm(request.POST, request.FILES)
        if form.is_valid():
            estadio = form.save(commit=False)
            estadio.author = request.user
            estadio.save()
            return redirect('estadios')
    else:
        form = EstadioForm()

    return render(request, 'BlogEstadiosApp/crear_estadio.html', {'form': form})


@login_required
def update_user_profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect(reverse_lazy('estadios'))
        else:
            messages.error(
                request, 'Hubo un error al actualizar el perfil. Verifica los datos.')

    else:
        form = UserProfileUpdateForm(instance=request.user.userprofile)

    return render(request, 'registration/update_profile.html', {'form': form})


class EstadioDeleteView(LoginRequiredMixin, DeleteView):
    model = Estadio
    template_name = 'BlogEstadiosApp/estadio_confirm_delete.html'
    success_url = reverse_lazy('estadios')


class EstadioUpdateView(UpdateView):
    model = Estadio
    template_name = 'BlogEstadiosApp/edit_estadio.html'
    form_class = EstadioForm
    success_url = reverse_lazy('estadios')
