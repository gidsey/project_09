from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View

from . import models
from . import forms


def menu_list(request):
    """List all menus whose expiry date is later than today."""
    menus = models.Menu.objects.all().prefetch_related('items').filter(
        expiration_date__gte=timezone.now()).order_by('-expiration_date')
    return render(request, 'menu/menu_list.html', {'menus': menus})


def menu_detail(request, pk):
    """Show the Menu details."""
    try:
        menu = models.Menu.objects.prefetch_related('items').get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_detail(request, pk):
    """Show the Item details."""
    try:
        item = models.Item.objects.prefetch_related('chef').get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'menu/item_detail.html', {'item': item})


@login_required
def create_new_menu(request):
    """Create a new menu, chosing from existing items."""
    """Create a new menu, chosing from existing items."""
    form = forms.MenuForm()
    if request.method == "POST":
        form = forms.MenuForm(data=request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            menu.items.set(form.cleaned_data['items'])
            messages.success(request, "Menu added successfully.")
            return redirect('menu:menu_detail', pk=menu.pk)
    return render(request, 'menu/menu_new.html', {
        'form': form,
    })


class MyEditMenu(View):

    form_class = forms.MenuForm
    # initial = {'items': selected_items}
    # instance = menu
    template_name = 'menu/menu_edit.html'

    def get(self, request, *args, **kwargs):
        try:
            menu = models.Menu.objects.prefetch_related('items').get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404
        selected_items = [item.id for item in menu.items.all()]

        form = self.form_class(initial=self.initial, instance=self.instance)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.instance)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            menu.items.set(form.cleaned_data['items'])
            messages.success(request, "Menu updated successfully.")
            return redirect('menu:menu_detail', pk=menu.pk)
        return render(request, 'menu/menu_edit.html', {
            # 'menu': menu,
            'form': form,
        })



# @login_required
# def edit_menu(request, pk):
#     """Edit an existing menu."""
#     try:
#         menu = models.Menu.objects.prefetch_related('items').get(pk=pk)
#     except ObjectDoesNotExist:
#         raise Http404
#
#     selected_items = [item.id for item in menu.items.all()]
#     form = forms.MenuForm(initial={'items': selected_items}, instance=menu)
#
#     if request.method == "POST":
#         form = forms.MenuForm(instance=menu, data=request.POST)
#         if form.is_valid():
#             menu = form.save(commit=False)
#             menu.created_date = timezone.now()
#             menu.save()
#             menu.items.set(form.cleaned_data['items'])
#             messages.success(request, "Menu updated successfully.")
#             return redirect('menu:menu_detail', pk=menu.pk)
#     return render(request, 'menu/menu_edit.html', {
#         'menu': menu,
#         'form': form,
#         })


@login_required
def delete_menu(request, pk):
    """Delete a menu and related references."""
    menu = get_object_or_404(models.Menu, pk=pk)
    form = forms.DeleteMenuForm(instance=menu)

    if request.method == "POST":
        form = forms.DeleteMenuForm(instance=menu, data=request.POST)
        if form.is_valid():
            menu.delete()
            messages.success(request, "Menu deleted successfully.")
            return HttpResponseRedirect(reverse('menu:menu_list'))
    return render(request, 'menu/menu_delete.html', {
        'menu': menu,
        'form': form,
        })
