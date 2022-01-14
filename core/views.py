from django.shortcuts import render
from django.views.generic import TemplateView
from core.forms import AddressForm
# Create your views here.
class home(TemplateView):
    template_name = 'temp.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = AddressForm
        context['form'] = fm
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print("errors are", form.errors)
        return HttpResponse("Hello")
