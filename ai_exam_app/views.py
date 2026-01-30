from django.shortcuts import render,redirect
from .import models
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
def admin_login(request):
    return render(request, 'admin_login.html')
def base(request):
    return render(request, 'base.html')
def cheating_report(request):
    return render(request, 'cheating_report.html')
def contact(request):
    return render(request, 'contact.html')
def exam_list(request):
    return render(request, 'exam_list.html')
def exam(request):
    return render(request, 'exam.html')
def monitor(request):
    return render(request, 'monitor.html')
def result(request):
    return render(request, 'result.html')
def signup(request):
    return render(request, 'signup.html')
def teacher_profile(request):
    if 'username' not in request.session:
        return redirect('teacher_login')
    username = request.session['username']
    teacher = models.Teacher.objects.get(username=username)
    return render(request, 'teacher_profile.html', {'teacher': teacher})
def student_dashboard(request):
    if 'username' not in request.session:
        return redirect('student_login')
    student = models.Student.objects.get(username=request.session['username'])
    return render(request, 'student_dashboard.html', {'student': student})
def teacher_dashboard(request):
    if 'username' not in request.session:
        return redirect('teacher_login')
    teacher = models.Teacher.objects.get(username=request.session['username'])
    return render(request, 'teacher_dashboard.html',{'teacher': teacher})

def stud_reg(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        registration_number = request.POST.get('registration_number')
        roll_number = request.POST.get('roll_number')
        semester = request.POST.get('semester')
        gender = request.POST.get('gender')
        department = request.POST.get('department')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if models.Student.objects.filter(username=username).exists():
            return HttpResponse("Username already taken. Please choose a different username.")
        else:
            student = models.Student(
                full_name=full_name,
                registration_number=registration_number,
                roll_number=roll_number,
                semester=semester,
                gender=gender,
                department=department,
                phone_no=phone_no,
                email=email,
                username=username,
                password=password
            )
            student.save()
            return redirect('login')
    return render(request,'student_registration.html')

def teach_reg(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        employee_id = request.POST.get('employee_id')
        age = request.POST.get('age')
        address = request.POST.get('address')
        department = request.POST.get('department')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if models.Teacher.objects.filter(username=username).exists():
            return HttpResponse("Username already taken. Please choose a different username.")
        else:
            teacher = models.Teacher(
                full_name=full_name,
                employee_id=employee_id,
                age=age,
                address=address,
                department=department,
                phone_no=phone_no,
                email=email,
                username=username,
                password=password
            )
            teacher.save()
            return redirect('login')
    return render(request,'teacher_registration.html')

def stud_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            student = models.Student.objects.get(username=username, password=password)
        except models.Student.DoesNotExist:
            return HttpResponse("Invalid credentials. Please try again.")
        print(student.full_name)
        if password == student.password:
            print("Login successful for student:", student.full_name)
            request.session['username'] = username
            return redirect('student_dashboard')
        else:
            return HttpResponse("Invalid credentials. Please try again.")
    return render(request, 'student_login.html')

def teach_login(request):
    hi = models.Teacher.objects.all().first()
    print(hi.username)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        try:
            teacher = models.Teacher.objects.get(username=username, password=password)
        except models.Teacher.DoesNotExist:
            return HttpResponse("Invalid credentials. Please try again.")
        if password == teacher.password:
            request.session['username'] = username
            return redirect('teacher_dashboard')
        else:
            return HttpResponse("Invalid credentials. Please try again.")
    return render(request, 'teacher_login.html')

def stud_profile(request):
    if 'username' not in request.session:
        return redirect('student_login')
    username = request.session['username']
    student = models.Student.objects.get(username=username)
    return render(request, 'student_profile.html', {'student': student})

def teach_profile(request):
    if 'username' not in request.session:
        return redirect('teacher_login')
    username = request.session['username']
    teacher = models.Teacher.objects.get(username=username)
    return render(request, 'teacher_profile.html', {'teacher': teacher})