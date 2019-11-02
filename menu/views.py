from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from operator import attrgetter
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from . import models

from . import forms


def menu_list(request):
    now = timezone.now()
    menus = models.Menu.objects.all().prefetch_related(
        'items'
        ).filter(expiration_date__gte=now).order_by('-expiration_date')
    return render(request, 'menu/menu_list.html', {'menus': menus})


def menu_detail(request, pk):
    menu = models.Menu.objects.prefetch_related('items').get(pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_detail(request, pk):
    try:
        item = models.Item.objects.prefetch_related('chef').get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'menu/item_detail.html', {'item': item})


def edit_item(request, pk):
    pass


def create_new_menu(request):
    form = forms.MenuForm()
    if request.method == "POST":
        form = forms.MenuForm(data=request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            selected_items = form.cleaned_data['items']
            menu.created_date = timezone.now()
            menu.save()
            menu.items.set(selected_items)
            return redirect('menu:menu_detail', pk=menu.pk)
    return render(request, 'menu/menu_new.html', {'form': form})


def edit_menu(request, pk):
    try:
        menu = models.Menu.objects.prefetch_related('items').get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404

    selected_items = [item.id for item in menu.items.all()]

    form = forms.MenuForm(initial={'items': selected_items}, instance=menu)

    if request.method == "POST":
        form = forms.MenuForm(instance=menu, data=request.POST)
        # menu.season = request.POST.get('season', '')
        # menu.expiration_date = request.POST.get('expiration_date', ''), '%m/%d/%Y'
        # menu.items = request.POST.get('items', '')
        # menu.save()
        # menu.items.set(request.POST.get('items', ''))

    return render(request, 'menu/menu_edit.html', {
        'menu': menu,
        'form': form,
        })
