from django.shortcuts import render, redirect, get_object_or_404
from .forms import StaffForm, UserRegisterForm, UserLoginForm, TextForm
from .models import User, Staff, Patient, illness, prescriptions
from django.contrib import auth, messages

def register_staff(request):
    if request.method == 'POST':
        form_1 = UserRegisterForm(request.POST)
        form_2 = StaffForm(request.POST)
        if form_1.is_valid() and form_2.is_valid():
            first_name = form_1.cleaned_data['first_name']
            last_name = form_1.cleaned_data['last_name']
            username = form_1.cleaned_data['username']
            email = form_1.cleaned_data['email']
            gender = form_1.cleaned_data['gender']
            department = form_2.cleaned_data['department']
            password1 = form_1.cleaned_data['password1']
            password2 = form_1.cleaned_data['password2']
            if password1 == password2:
                #Check Username
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That Username is already taken')
                    return redirect('register_staff')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'That email is being used')
                        return redirect('register_staff')
                    else:
                        #looks good
                        user = User.objects.create_user(first_name = first_name, last_name = last_name, username=username, email=email, is_staff = True,
                                                   password = password1)
                        user.save()
                        staff = Staff.objects.create(user_id = user.id, first_name = first_name, last_name = last_name, username = username,
                                                      email=email, gender=gender, department=department)
                        staff.save()
                        messages.success(request, 'Staff User Created Succesfully, You can login now')
                        return redirect('login')

            else:
                messages.error(request, 'Passwords Do Not Match')
                return redirect('register_staff')
    else:
        form_2 = StaffForm()
        form_1 = UserRegisterForm()   
        context = {
            'staff_form': form_2,
            'user_form': form_1
        }
        return render(request, 'accounts/register_staff.html', context)

def register_patient(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            password = form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            if password == password2:
                #Check Username
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That Username is already taken')
                    return redirect('register_patient')
                else:
                    #Check Email
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'That email is being used')
                        return redirect('register_patient')
                    else:
                        # Looks Good
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password,
                                                   is_patient=True)
                        user.save()
                        patient = Patient.objects.create(user_id=user.id, first_name=first_name, last_name=last_name, username=username, email=email, 
                                                         gender=gender)
                        patient.save()
                        messages.success(request, 'User Created Succesfully, You can login now')
                        return redirect('login')

            else:
                messages.error(request, 'Passwords Do Not Match')
                return redirect('register_patient')
    else:
        form = UserRegisterForm()
        context = {
            'user_form': form
        }
        return render(request, 'accounts/register_patient.html', context)

def login(request):
    login_form = UserLoginForm()
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(
                username= login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password'],
            )
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('index')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('login')    
    context = {
        'login_form': login_form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user.is_patient == True:
        visitor_user = request.user
        patient = get_object_or_404(Patient, pk=user_id)
        illnesses = illness.objects.filter(patient_id=user_id)
        Prescriptions = prescriptions.objects.filter(patient_id=user_id)
        context = {
            'patient': patient,
            'user': visitor_user,
            'illnesses': illnesses,
            'Prescriptions': Prescriptions
        }
        return render(request, 'accounts/patient_profile.html', context)
    elif user.is_staff == True:
        staff = get_object_or_404(Staff, pk=user_id)
        context = {
            'staff': staff,
        }
        return render(request, 'accounts/staff_profile.html', context)

def add_illness(request, user_id):
    form = TextForm()
    patient = get_object_or_404(Patient, pk=user_id)
    user = request.user
    if user.is_staff:
            if request.method == 'POST':
                form = TextForm(request.POST)
                if form.is_valid():
                    text = form.cleaned_data['text']
                    Illness = illness.objects.create(illness=text, patient_id=patient.pk, doctor_id=user.pk)
                    Illness.save()
                    messages.success(request, 'Illness has been added')
                    return redirect('profile', user_id)
    else:
        messages.error(request, 'You are not a Staff User')
        return redirect('profile')
    context = {
        'form': form
    }
    return render(request, 'accounts/add_illness.html', context)

def add_prescription(request, user_id):
    form = TextForm()
    patient = get_object_or_404(Patient, pk=user_id)
    user = request.user
    if user.is_staff:
            if request.method == 'POST':
                form = TextForm(request.POST)
                if form.is_valid():
                    text = form.cleaned_data['text']
                    Prescription = prescriptions.objects.create(prescriptions=text, patient_id=patient.pk, doctor_id=user.pk)
                    Prescription.save()
                    messages.success(request, 'Prescription has been added')
                    return redirect('profile', user_id)
    else:
        messages.error(request, 'You are not a Staff User')
        return redirect('profile')
    context = {
        'form': form
    }
    return render(request, 'accounts/add_prescriptions.html', context)