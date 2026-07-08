from django.shortcuts import render ,redirect,get_object_or_404
from .models import Student
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def dashboard(request):
    students = Student.objects.all()
    return render(request, 'dashboard.html',{'students':students})

def add_student(request):
    if request .method== "POST":
        name = request .POST.get('name')
        course = request .POST.get('course')
        age = request .POST.get('age')
        gender = request .POST.get('gender')
        email = request .POST.get('email')

        Student .objects.create(
            name = name,
            course = course,
            age = age,
            gender = gender,
            email = email,
        )
        return redirect("dashboard")
    return render(request, 'add_student.html')

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST.get('name')
        student.course = request.POST.get('course')
        student.age = request.POST.get('age')
        student.gender = request.POST.get('gender')
        student.email = request.POST.get('email')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, 'register.html',
                   {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("dashboard")

def logout_view(request):
    logout(request)
    return redirect('login')