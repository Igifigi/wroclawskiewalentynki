from django.shortcuts import render, redirect

def chat(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {}
    return render(request, 'chat.html', context)

