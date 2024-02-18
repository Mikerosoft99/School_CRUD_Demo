from django.shortcuts import get_object_or_404, redirect, render
from day2.models import Student, User
from django.contrib import messages

# Create your views here.

def home(request):
    # print(request.session.items())
    if 'user_email' in request.session:
        return render(request, 'day2/home.html')
    else:
        messages.error(request, 'You need to sign in first.')
        return redirect("signin")

def students(request):
    if 'user_email' in request.session:
        students = Student.objects.all()
        return render(request, 'day2/students.html',{'students': students})
    else:
        messages.error(request, 'You need to sign in first.')
        return redirect("signin")

def create_student(request):
        if 'user_email' in request.session:
            if request.method == 'POST':
                f_name = request.POST['f_name'].title()
                l_name = request.POST['l_name'].title()
                age = request.POST['age']

                Student.objects.create(f_name=f_name, l_name=l_name, age=age)
                messages.success(request, 'Student created successfully.')

                return redirect('students')
            return render(request, 'day2/create_student.html')
        else:
            messages.error(request, 'You need to sign in first.')
            return redirect("signin")

def delete_student(request,id):
    Student.objects.get(id=id).delete()
    messages.success(request, 'Student deleted successfully.')

    return redirect('students')
        
def update_student(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)

    if request.method == 'GET':
        return render(request, 'day2/update_student.html', {'student': student})

    elif request.method == 'POST':
        student.f_name = request.POST['f_name'].title()
        student.l_name = request.POST['l_name'].title()
        student.age = request.POST['age']
        student.save()
        messages.success(request, 'Student updated successfully.')

        return redirect('students')

def signup(request):
    if request.method == 'GET':
        return render(request, 'day2/signup.html')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name'].title()

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already signed up! You can try signing in.')
            return render(request, 'day2/signup.html')

        user = User.objects.create(email=email, password=password, name=name)
        messages.success(request, 'Congratulations, You can signing in now.')

        return redirect("signin")

def signin(request):
    if request.method == 'GET':
        return render(request, 'day2/signin.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                request.session['user_email'] = email
                messages.success(request, f'Hello, {user.name}')
                return redirect("home")
            else:
                messages.error(request, 'Incorrect password. Please try again.')
                return render(request, 'day2/signin.html')
        except:
            messages.error(request, "This email doesn't exist. Please sign up first.")
            return render(request, 'day2/signin.html')

def signout(request):
    request.session.clear()
    return redirect("signin")

def about(request):
    return render(request, "day2/about.html")