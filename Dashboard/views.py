from django.shortcuts import render ,redirect,get_object_or_404
from .models import Student

# Create your views here.
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

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("dashboard")
