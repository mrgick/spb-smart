from django.shortcuts import render, reverse, get_object_or_404, redirect, HttpResponse
from offer.models import Offer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin 
from offer.forms import *
from django.core.paginator import Paginator

#homepage
def home(request):
    return render(request, 'offer/home.html')

#offers show
def offers(request,of_type,page_titile):
    offers = Offer.objects.all().filter(oftype=of_type)

    paginator = Paginator(offers, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'page_titile':page_titile,
    }

    return context
    

#top offers
def top_offers(request):
    of_type="ac"
    template='offer/offers_show.html'
    page_titile = "Топ предложений"
    context=offers(request, of_type, page_titile)
    return render(request, template, context)

#offers in the process
def inproc_offers(request):
    of_type="ip"
    template='offer/offers_show.html'
    page_titile = "В процессе"
    context=offers(request, of_type, page_titile)
    return render(request, template, context)


#offers archive
def archive_offers(request):
    of_type="ar"
    template='offer/offers_show.html'
    page_titile = "Архив"
    context=offers(request, of_type, page_titile)
    return render(request, template, context)


#signup - registration acc
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#offer show 
class OfferDetail(View):
    model = Offer
    template = 'offer/offer_detail.html'

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__exact=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj,
                                               'admin_object': obj,
                                               'detail': True})
#offer create
class OfferCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = OfferForm()

        return render(request, 'offer/offer_create.html', {'form': form})

    def post(self, request):
        bound_form = OfferForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('top_offers_url')
        return render(request, 'offer/offer_create.html', {'form': bound_form})

class OfferUpdate(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request, slug):
        if request.user.is_staff:
            offer = Offer.objects.get(slug__iexact=slug)
            bound_form = OfferForm(instance=offer)
            return render(request, 'offer/offer_update.html', {'form': bound_form, 'offer': offer})

    def post(self, request, slug):
        if request.user.is_staff:
            offer = Offer.objects.get(slug__iexact=slug)
            bound_form = OfferForm(request.POST, instance=offer)

            if bound_form.is_valid():
                new_post = bound_form.save()
                return redirect('top_offers_url')
            return render(request, 'offer/offer_update.html', {'form': bound_form, 'offer': offer})


def rate_offer(request):
    
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            pk = int(request.POST.get('offer_pk', ''))
            rate = 1 if request.POST.get('ispositive', '') == 'true' else -1
            curoffer = Offer.objects.get(pk=pk)
            
            response = ''
            oldrate = curoffer.has_user_rated(user)
            if oldrate == None:
                curoffer.add_user_rated(user, rate)
                curoffer.rating += rate
                response = 'true,false' if rate > 0 else 'false,true'
            elif (rate > 0 and oldrate < 0) or (rate < 0 and oldrate > 0):
                curoffer.rating += rate - oldrate
                curoffer.delete_user_rated(user) 
                curoffer.add_user_rated(user, rate) 
                response = 'true,false' if rate > 0 and oldrate < 0 else 'false,true'
            else:
                curoffer.rating -= oldrate
                curoffer.delete_user_rated(user)
                response = 'false,false'
           
            curoffer.save()
            
            return HttpResponse(response)
    return HttpResponse('error')