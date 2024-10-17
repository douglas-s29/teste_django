from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task, TimeEntry
from .forms import TaskForm, CustomUserCreationForm
from .forms import TimeEntryForm
from django_filters.views import FilterView
from .filters import TimeEntryFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import timedelta
from django.utils.timezone import localtime
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Você já pode fazer login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tarefas/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'tarefas/home.html')

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('tasks')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = TaskForm()
    return render(request, 'tarefas/create_task.html', {'form': form})

@login_required
def tasks(request):
    search = request.GET.get('search', '')

    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user)

    if search:
        try:
            # Tenta converter a pesquisa para uma data, sem hora
            search_date = datetime.strptime(search, '%d/%m/%Y').date()
        except ValueError:
            search_date = None

        # Filtra considerando todos os campos possíveis, incluindo busca flexível por data
        tasks = tasks.filter(
            Q(id__icontains=search) |
            Q(titulo__icontains=search) |
            Q(user__username__icontains=search) |
            Q(descricao__icontains=search) |
            (Q(data_criacao__date=search_date) if search_date else Q()) |
            (Q(inicio__date=search_date) if search_date else Q()) |
            (Q(fim__date=search_date) if search_date else Q())
        )

    # Calcular o tempo gasto para cada tarefa
    for task in tasks:
        if task.inicio and task.fim:
            delta = task.fim - task.inicio
            days = delta.days
            hours, remainder = divmod(delta.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            task.tempo_gasto = f'{days}d {hours}h {minutes}min {seconds}s'
        else:
            task.tempo_gasto = 'Em andamento'

    return render(request, 'tarefas/tasks.html', {'tasks': tasks})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # Garantir que a data de início não seja alterada
            form.instance.inicio = task.inicio
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tarefas/edit_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('tasks')
    return render(request, 'tarefas/delete_task.html', {'task': task})


@login_required
def list_time_entries(request):
    time_entries = TimeEntry.objects.filter(task__user=request.user)
    # Implementar filtragem aqui
    return render(request, 'tarefas/time_entries.html', {'time_entries': time_entries})

@login_required
def create_time_entry(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            time_entry = form.save(commit=False)
            time_entry.task = task
            time_entry.save()
            return redirect('list_time_entries')
    else:
        form = TimeEntryForm()
    return render(request, 'tarefas/create_time_entry.html', {'form': form, 'task': task})

class TimeEntryListView(LoginRequiredMixin, FilterView):
    model = TimeEntry
    template_name = 'tarefas/time_entries.html'
    context_object_name = 'time_entries'
    filterset_class = TimeEntryFilter

    def get_queryset(self):
        return TimeEntry.objects.filter(task__user=self.request.user)
    

class CustomLoginView(auth_views.LoginView):
    template_name = 'tarefas/login.html'

    def form_invalid(self, form):
        return super().form_invalid(form) 
    

# Gerenciar usuários
@user_passes_test(lambda u: u.is_superuser)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'tarefas/manage_users.html', {'users': users})

# Excluir usuários
@user_passes_test(lambda u: u.is_superuser)  # Apenas superusuários podem acessar
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('manage_users')

# Alternar permissão de admin (staff)
@user_passes_test(lambda u: u.is_superuser)  # Apenas superusuários podem acessar
def toggle_admin(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        # Alternar o status de admin
        if 'is_admin' in request.POST:
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False
        user.save()
    return redirect('manage_users')