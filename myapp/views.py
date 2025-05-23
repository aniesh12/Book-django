from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Item

from .forms import FormItem
# Create your views here.


def home(request):
    return render(request,'book.html')


def send(request):
    if request.method == "POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        published=request.POST.get('published')
        isbn=request.POST.get('isbn')
        summary=request.POST.get('summary')

        user=Item.objects.create(
            title=title,author=author,published=published,isbn=isbn,summary=summary
        )

        user.save()
        print(f'Item creat {title}')
        return HttpResponse('done')
    return HttpResponse('invlied')

def ListView(request):
    items = Item.objects.all()
    return render(request,'data.html' ,{"data":items})



def Upadte(request, pk):
    item = get_object_or_404(Item, id=pk)

    if request.method == 'POST':
        form = FormItem(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = FormItem(instance=item)

    return render(request, 'upadte.html', {'form': form})



def delete_it(request,pk):

    item=get_object_or_404(Item,id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('data')
    return render(request, 'confirm_delete.html', {'data': item})
