from django.shortcuts import render
from mainapp.forms import NameForm, ContactForm, NewsLetterForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def index_view(request):
    return render(request, 'website/index.html',{'phone':'09372494703',
                                                 'email':'shahin.it.org@gmail.com',
                                                 'address':'ایران ، جیرفت ، همین اطراف'})
    
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد ، به زودی با شما تماس خواهیم گرفت!')
            return HttpResponseRedirect('/')

    form = ContactForm()
    context = {'form':form,'phone':'09136358518','email':'shahin.it.org@gmail.com','address':'جیرفت ، همین اطراف'}
    return render (request,'website/contact.html', context)
    
def about_view(request):
    return render(request, 'website/about.html',{'phone':'09372494703',
                                                 'email':'shahin.it.org@gmail.com',
                                                 'address':'کرمان ، جیرفت ، هند کوچک'})
    
    
def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'درخواست شما برای خبرنامه با موفقیت ارسال شد!')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
    

def custom_404(request, exception):
    return render(request, '404.html', status=404)