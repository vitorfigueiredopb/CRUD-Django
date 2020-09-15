from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Console
from .forms import ConsoleForm

# view para listar os consoles
class ListConsoles(ListView):
    model = Console
    template_name = 'consoles/list_consoles.html'
    context_object_name = 'consoles'

# view para adcionar um novo console
class CreateConsole(CreateView):
    model = Console
    template_name = 'consoles/create_console.html'
    form_class = ConsoleForm
    success_url = reverse_lazy('list_consoles')

# view para editar um console existente
class UpdateConsole(UpdateView):
    model = Console
    template_name = 'consoles/update_console.html'
    form_class = ConsoleForm
    success_url = reverse_lazy('list_consoles')

# view para deletar um console
class DeleteConsole(DeleteView):
    model = Console
    success_url = reverse_lazy('list_consoles')