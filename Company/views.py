from email import message
import datetime
from http.client import CONTINUE
from django.core.exceptions import ValidationError
from django.core.mail import BadHeaderError, send_mail
from multiprocessing import context
from multiprocessing.dummy import JoinableQueue
from ntpath import join
from operator import attrgetter, truediv
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from django.contrib.auth.decorators import login_required
from Agent.models import *
from .form import passwordform, NameForm
from django.core.mail import send_mail
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import Group
from Customer.models import Customer_order
from django.conf import settings

# Create your views here.


def Admin_dashboard(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            all_agent = Agent.objects.all()
            S_staff = Company_Store_Manager.objects.all()
            F_staff = Finance_Manager.objects.all()
            total_agent = 0
            for agent in all_agent:
                if agent.user.is_active:
                    total_agent += 1
            tottal_staff = S_staff.count() + F_staff.count()
            all_store = Company_Store.objects.all()
            tottal_store = all_store.count()
            all_region = Region.objects.all()
            tottal_region = all_region.count()
            all_product = ProductNew.objects.all()
            tottal_product = all_product.count()
            adds = Advertisment.objects.all()

            context = {
                'all_agent': all_agent,
                'total_agent': total_agent,
                'tottal_staff': tottal_staff,
                'tottal_store': tottal_store,
                'tottal_region': tottal_region,
                'tottal_product': tottal_product,
                'all_product': all_product,
                'adds': adds,

            }

            return render(request, 'Company/dashboard/admin.html', context)

        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login before')
        return redirect('logout')


def staff_dashboard(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            all_agent = Agent.objects.all()
            S_staff = Company_Store_Manager.objects.all()
            F_staff = Finance_Manager.objects.all()
            total_agent = all_agent.count()
            tottal_staff = S_staff.count() + F_staff.count()
            all_store = Company_Store.objects.all()
            tottal_store = all_store.count()
            all_region = Region.objects.all()
            tottal_region = all_region.count()
            all_product = ProductNew.objects.all()
            tottal_product = all_product.count()
            staff_finance_manager = Finance_Manager.objects.all()
            staff_company_store_manager = Company_Store_Manager.objects.all()
            adds = Advertisment.objects.all()
           
            
            context = {
                
                'all_agent': all_agent,
                'total_agent': total_agent,
                'tottal_staff': tottal_staff,
                'tottal_store': tottal_store,
                'tottal_region': tottal_region,
                'tottal_product': tottal_product,
                'all_product': all_product,
                'staff_finance_manager': staff_finance_manager,
                'staff_company_store_manager': staff_company_store_manager,
                'adds':adds,

            }
            return render(request, 'Company/dashboard/staff.html', context)
        else:
            return redirect('login')

    except IndexError as e:
        messages.error(request, 'Login before')
        return redirect('logout')


def store_dashboard(request):
    if request.user.is_authenticated:
        if request.user.groups.exists():
            a = request.user.groups.all()[0].name
            if a == 'Admin':
                all_agent = Agent.objects.all()
                S_staff = Company_Store_Manager.objects.all()
                F_staff = Finance_Manager.objects.all()
                total_agent = all_agent.count()
                tottal_staff = S_staff.count() + F_staff.count()
                all_store = Company_Store.objects.all()
                tottal_store = all_store.count()
                all_region = Region.objects.all()
                tottal_region = all_region.count()
                all_product = ProductNew.objects.all()
                tottal_product = all_product.count()
                staff_finance_manager = Finance_Manager.objects.all()
                staff_company_store_manager = Company_Store_Manager.objects.all()
                adds = Advertisment.objects.all()
                context = {
                    'all_agent': all_agent,
                    'total_agent': total_agent,
                    'tottal_staff': tottal_staff,
                    'all_store': all_store,
                    'tottal_store': tottal_store,
                    'tottal_region': tottal_region,
                    'tottal_product': tottal_product,
                    'all_product': all_product,
                    'staff_finance_manager': staff_finance_manager,
                    'staff_company_store_manager': staff_company_store_manager,
                    'adds':adds,
                }
                return render(request, 'Company/dashboard/store.html', context)
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return redirect('login')


def region_dashboard(request):
    if request.user.is_authenticated:
        if request.user.groups.exists():
            a = request.user.groups.all()[0].name
            if a == 'Admin':
                all_agent = Agent.objects.all()
                S_staff = Company_Store_Manager.objects.all()
                F_staff = Finance_Manager.objects.all()
                total_agent = all_agent.count()
                tottal_staff = S_staff.count() + F_staff.count()
                all_store = Company_Store.objects.all()
                tottal_store = all_store.count()
                all_region = Region.objects.all()
                tottal_region = all_region.count()
                all_product = ProductNew.objects.all()
                tottal_product = all_product.count()
                staff_finance_manager = Finance_Manager.objects.all()
                staff_company_store_manager = Company_Store_Manager.objects.all()
                adds = Advertisment.objects.all()
                context = {
                    'all_agent': all_agent,
                    'total_agent': total_agent,
                    'tottal_staff': tottal_staff,
                    'all_store': all_store,
                    'all_region': all_region,
                    'tottal_store': tottal_store,
                    'tottal_region': tottal_region,
                    'tottal_product': tottal_product,
                    'all_product': all_product,
                    'staff_finance_manager': staff_finance_manager,
                    'staff_company_store_manager': staff_company_store_manager,
                    'adds':adds,

                }
                return render(request, 'Company/dashboard/region.html', context)
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return redirect('login')


def product_dashboard(request):
    all_agent = Agent.objects.all()
    S_staff = Company_Store_Manager.objects.all()
    F_staff = Finance_Manager.objects.all()
    total_agent = all_agent.count()
    tottal_staff = S_staff.count() + F_staff.count()
    all_store = Company_Store.objects.all()
    tottal_store = all_store.count()
    all_region = Region.objects.all()
    tottal_region = all_region.count()
    all_product = ProductNew.objects.all()
    tottal_product = all_product.count()
    staff_finance_manager = Finance_Manager.objects.all()
    staff_company_store_manager = Company_Store_Manager.objects.all()
    adds = Advertisment.objects.all()
    context = {
        'all_agent': all_agent,
        'total_agent': total_agent,
        'tottal_staff': tottal_staff,
        'all_store': all_store,
        'all_region': all_region,
        'tottal_store': tottal_store,
        'tottal_region': tottal_region,
        'tottal_product': tottal_product,
        'all_product': all_product,
        'staff_finance_manager': staff_finance_manager,
        'staff_company_store_manager': staff_company_store_manager,
        'adds':adds

    }
    return render(request, 'Company/dashboard/product.html', context)


def add_agent(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            all_region = Region.objects.all()
            if request.method == 'POST':
                errorr = request.POST.get('error')
                # required
                region = request.POST.get('region')
                city = request.POST.get('city')
                address = request.POST.get('address')
                location = request.POST.get('location')
                TIN_NO = request.POST.get('TIN_NO')
                marchent_id = request.POST.get('marchent_id')
                agreement = request.FILES.get('agreement')
                license = request.FILES.get('license')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                username = request.POST.get('username')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                phone1 = request.POST.get('phone1')
                # check if it the followings are empty
                phone1 = '+251' + phone1
                phone2 = request.POST.get('phone2')
                phone2 = '+251' + phone2
                facebook = request.POST.get('facebook')
                telegram = request.POST.get('telegram')
                instagram = request.POST.get('instagram')
                about = request.POST.get('about')
                profile = request.FILES.get('profile')
                if errorr == '':
                    if password1 == password2:
                        new = User.objects.filter(username=username)
                        if new.count():
                            messages.error(request, "User Already Exist")
                        else:
                            new = User.objects.filter(email=email)
                            if new.count():
                                messages.error(request, "email Already Exist")
                            else:
                                rregion = Region.objects.get(
                                    Region_Name=region)
                                user = User.objects.create_user(
                                    username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                                my_group = Group.objects.get(name='Agent')
                                my_group.user_set.add(user)
                                if user:
                                    agent = Agent.objects.create(user=user, Full_Name=first_name+' '+last_name, phone1=phone1, phone2=phone2, facebook=facebook, telegram=telegram,
                                                                 instagram=instagram, about=about, profile_pic=profile, Region=rregion, TIN_NO=TIN_NO, location=location, address=address, city=city,
                                                                 marchentId=marchent_id, agreement=agreement, License=license)
                                    if agent:
                                        subject = 'Welcome to BGI-Ethiopia'
                                        message = 'Dear '+ first_name + '\n' + 'Your username and password are: ' + '\n'  +'username:- '+ username + '\n' + 'password:- ' + password1 + '\n' + 'Thanks for joining us' + '\n' + 'Lgin here ' + 'http://192.168.1.5:8002:8002/'
                                        print(message)
                                        to_email = email
                                        from_email = settings.EMAIL_HOST_USER
                                        if subject and message and to_email and from_email:
                                            try:
                                                send_mail(subject, message, from_email,[to_email],fail_silently=False,)
                                            except BadHeaderError:
                                                return HttpResponse('Invalid header found.')
                                        messages.success(
                                            request, 'Agent registered successfully!')
                                        return redirect('agent-view')
                    else:
                        messages.error(request, 'password didn\'t match.')

                else:
                    messages.error(request, 'Please, fill the form correctly.')

                context = {
                    'region': region,
                    'city': city,
                    'address': address,
                    'location': location,
                    'TIN_NO': TIN_NO,
                    'marchent_id': marchent_id,
                    'agreement': agreement,
                    'license': license,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'username': username,
                    'password1': password1,
                    'phone1': phone1,
                    'phone2': phone2,
                    'facebook': facebook,
                    'telegram': telegram,
                    'instagram': instagram,
                    'about': about,
                    'profile': profile,
                    'all_region': all_region,



                }
                return render(request, 'Company/agents/add-agent.html', context)

            return render(request, 'Company/agents/add-agent.html', {'all_region': all_region})
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before')
        return redirect('logout')


# Profile
def show_profile(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            users = User.objects.get(id=request.user.id)
            admin = users.admin
            print(admin)
            context = {
                'admin': admin,
            }
            return render(request, 'Company/profile/show_profile.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def edit_profile(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            users = User.objects.get(id=request.user.id)
            admin = users.admin
            context = {
                'admin': admin,

            }
            if request.method == 'POST':
                admin.about = request.POST['about']
                admin.phone1 = request.POST['phone']
                admin.Company = request.POST['company']
                admin.Country = request.POST['country']
                admin.Job = request.POST['job']
                admin.address = request.POST['address']
                admin.facebook = request.POST['facebook']
                admin.telegram = request.POST['telegram']
                admin.instagram = request.POST['instagram']
                users.first_name = request.POST['first_name']
                users.last_name = request.POST['last_name']
                users.email = request.POST['email']
                admin.save()
                users.save()
                return redirect('show_profile')
            return render(request, 'Company/profile/edit_profile.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def change_password(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            users = User.objects.get(id=request.user.id)
            admin = users.admin

            if request.method == 'POST':
                form = passwordform(request.user, request.POST)
                if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)  # Important!
                    messages.success(
                        request, 'Your password was successfully updated!')
                    return redirect('show_profile')
                else:
                    messages.error(request, 'Please correct the error below.')
            else:
                form = passwordform(request.user)
            context = {
                'admin': admin,
                'usermodel': users,
                'form': form
            }
            return render(request, 'Company/profile/chage_password.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def change_profile_pic(request):

    try:
        if request.user.groups.all()[0].name == 'Admin':
            users = User.objects.get(id=request.user.id)
            admin = users.admin
            context = {
                'admin': admin,
                'usermodel': users
            }
            if request.method == 'POST':
                if len(request.FILES['img']) != 0:
                    admin.profile_pic.delete()
                    admin.profile_pic = request.FILES['img']
                    admin.save()
                    return redirect('edit_profile')
                else:
                    return render(request, 'Company/profile/change_profile_pic.html', context)
            return render(request, 'Company/profile/change_profile_pic.html', context)

        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def delete_profile_pic(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            users = User.objects.get(id=request.user.id)
            admin = users.admin
            context = {
                'admin': admin,
                'usermodel': users
            }
            if len(admin.profile_pic) != 0:
                admin.profile_pic.delete()
                return redirect('edit_profile')

            return render(request, 'Company/profile/edit_profile.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')
# end profile

# //////////////

# Manage Staff


def view_staff(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            staff_finance_manager = Finance_Manager.objects.all()
            staff_company_store_manager = Company_Store_Manager.objects.all()
            context = {
                'staff_finance_manager': staff_finance_manager,
                'staff_company_store_manager': staff_company_store_manager,
            }
            return render(request, 'Company/staffs/staff-view.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def staff_profile(request, pk, staff):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            if staff == 'Finance_manager' or 'F' in staff:
                staff_detail = Finance_Manager.objects.get(id=pk)
                context = {'staff_detail': staff_detail}
            elif staff == 'Store_Manager' or 'S' in staff:
                staff_detail = Company_Store_Manager.objects.get(id=pk)
                context = {'staff_detail': staff_detail}
            else:
                context = {}
            return render(request, 'Company/staffs/staff-detail.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def staff_remove_page(request, pk, staff):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            if staff == 'Finance_manager' or 'F' in staff:
                staff_detail = Finance_Manager.objects.get(id=pk)
                if staff_detail.user.is_active:
                    staff_detail.user.is_active = False
                else:
                    messages.error(request, staff_detail.user.username +
                                   ' is already deactivated!')
                staff_detail.user.save()
            elif staff == 'Store_Manager' or 'S' in staff:
                staff_detail = Company_Store_Manager.objects.get(id=pk)
                if staff_detail.user.is_active:
                    staff_detail.user.is_active = False
                    staff_detail.user.save()
                else:
                    messages.error(request, staff_detail.user.username +
                                   ' is already deactivated!')
            return redirect('deleted_account')
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def add_staff(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            groups = Group.objects.all()
            context = {'groups': groups}
            if request.method == 'POST':
                first_name = request.POST.get('fn')
                last_name = request.POST.get('ln')
                username = request.POST.get('un')
                email = request.POST.get('email')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                facebook = request.POST.get('facebook')
                telegram = request.POST.get('telegram')
                instagram = request.POST.get('instagram')
                phone = request.POST.get('phone1')
                position = request.POST.get('position')
                profile = request.FILES.get('profile')
                error = request.POST.get('error')
                address = request.POST.get('address')
                salary = request.POST.get('salary')
                about = request.POST.get('about')
                context = {

                    'address': address,

                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'username': username,
                    'password1': password1,
                    'phone': phone,
                    'facebook': facebook,
                    'telegram': telegram,
                    'instagram': instagram,
                    'about': about,
                    'profile': profile,
                    'groups': groups,




                }
                if error == '':
                    if password1 == password2:
                        new = User.objects.filter(username=username)
                        new1 = User.objects.filter(email=email)
                        if new.count() != 0:
                            messages.error(request, "User Already Exist")
                        if new1.count() != 0:
                            messages.error(request, "Email Already Exist")
                        elif new.count() == 0 and new1.count() == 0:
                            user = User.objects.create_user(
                                username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                            my_group = Group.objects.get(name=position)
                            my_group.user_set.add(user)
                            if user and position == 'Store_Manager':
                                company_Store_Manager = Company_Store_Manager.objects.create(user=user, Full_Name=first_name+' '+last_name, phone=phone, facebook=facebook, Telegram=telegram,
                                                                                             instagram=instagram, about=about, profile_pic=profile, address=address, salary=salary)
                                if company_Store_Manager:
                                    # successfully registered
                                    messages.success(
                                        request, "Company Store Manager ,successfully registered")
                                    return redirect('view-staff')
                                else:
                                    user.delete()
                                    messages.error(
                                        request, "Something went wrong,try again later")

                            elif user and position == 'Financ_admin':
                                Financ_admin = Finance_Manager.objects.create(user=user, Full_Name=first_name+' '+last_name, phone=phone, facebook=facebook, telegram=telegram,
                                                                              instagram=instagram, about=about, profile_pic=profile, address=address, salary=salary)
                                if Financ_admin:
                                    # successfully registered
                                    messages.success(
                                        request, "Finance Admin ,successfully registered")
                                    return redirect('view-staff')
                                else:
                                    user.delete()
                                    messages.error(
                                        request, "Something went wrong,try again later")
                    else:
                        messages.error(request, "password didn\'t match")
                else:
                    messages.error(request, "please ,fill the form correctly")

            return render(request, 'Company/staffs/add-staff.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def update_staff(request, pk, staff):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            if staff == 'Finance_manager':
                staff_detail = Finance_Manager.objects.get(id=pk)

                context = {'staff_detail': staff_detail}
                if request.method == 'POST':
                    #  staff_detail.staff=request.POST['job']
                    staff_detail.salary = request.POST['salary']
                    staff_detail.save()
                    messages.success(request, 'Store Manager updated')
                    return redirect('view-staff')

            elif staff == 'Store_Manager':
                staff_detail = Company_Store_Manager.objects.get(id=pk)
                stores = Company_Store.objects.all()
                context = {'staff_detail': staff_detail,
                           'stores': stores,
                           }
                if request.method == 'POST':
                    #  staff_detail.staff=request.POST['job']
                    staff_detail.salary = request.POST['salary']
                    staff_detail.Store = Company_Store.objects.get(
                        Store_Name=request.POST['store'])
                    staff_detail.save()
                    messages.success(request, 'Store Manager updated')
                    return redirect('view-staff')

            else:
                context = {}

            return render(request, 'Company/staffs/update_staff.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def remove_staff(request, pk, staff):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            if staff == 'Finance_manager':
                staff_detail = Finance_Manager.objects.get(id=pk)
                context = {'staff_detail': staff_detail}
            elif staff == 'Store_Manager':
                staff_detail = Company_Store_Manager.objects.get(id=pk)
                context = {'staff_detail': staff_detail}
            else:
                context = {}
            return render(request, 'Company/staffs/remove_staff.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')

# end Staff

# deleted account


def deleted_account(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            deleted_accounts = []
            all_user = User.objects.all()
            for user in all_user:
                if not user.is_active:
                    deleted_accounts.append(user)
            context = {
                'deleted_accounts': deleted_accounts,
            }
            return render(request, 'Company/deleted_account.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def permalent_delete(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            user = User.objects.get(pk=pk)
            messages.success(request, user.first_name + ' ' +
                             user.last_name + ' permalently Removed!')
            user.delete()
            deleted_accounts = []
            all_user = User.objects.all()
            for user in all_user:
                if not user.is_active:
                    deleted_accounts.append(user)

            context = {
                'deleted_accounts': deleted_accounts,
            }
            return render(request, 'Company/deleted_account.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')
# end deleted account


def view_agent_orders(request):
    return HttpResponse('agent orders')


def approve_agent_orders(request):
    return HttpResponse('agent orders approved')


def store(request):
    return HttpResponse('store')


def contact_store_manager(request):
    return HttpResponse('contact store manager')


def agent_report(request):

    return HttpResponse('agent report')


def finance_report(request):
    return HttpResponse('finance report')


def advertisements(request):
    return HttpResponse('addvertisment')

# agent management


def agent_view(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            all_agent = Agent.objects.all()
            context = {
                'all_agent': all_agent,
            }
            return render(request, 'Company/agents/agent-view.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def agent_detail(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            agent = Agent.objects.get(id=pk)
            print(agent)
            orders = Agent_order.objects.filter(Agent=agent)
            all_transaction = []
            for order in orders:
                all_transaction.append(
                    Agent_Transaction.objects.get(Agent_order_id=order.id))

            # all_transaction = Agent_Transaction.objects.filter().order_by('-date_created')
            # context = {
            #     'all_transaction': all_transaction,
            # }

            context = {
                'agent': agent,
                'all_transaction': all_transaction,
            }
            return render(request, 'Company/agents/agent-detail.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def agent_update_contrat(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            agent = Agent.objects.get(pk=pk)
            if request.method == 'POST':
                file = request.FILES.get('file')
                agent.agreement = file
                agent.last_updated = datetime.datetime.now()
                agent.save()

            context = {
                'agent': agent,
            }
            return render(request, 'Company/agents/update_agent.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def remove_agent_page(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            agent = Agent.objects.get(pk=pk)

            context = {
                'agent': agent,
            }
            return render(request, 'Company/agents/remove_agent.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def remove_agent(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            agent = Agent.objects.get(pk=pk)
            agent.user.is_active = False
            agent.user.save()
            deleted_accounts = []
            all_user = User.objects.all()
            for user in all_user:
                if not user.is_active:
                    deleted_accounts.append(user)

            messages.info(request, agent.user.first_name + ' ' +
                          agent.user.last_name + ' is now Removed')
            context = {
                'deleted_accounts': deleted_accounts,
            }
            return render(request, 'Company/deleted_account.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def re_active_account(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            user = User.objects.get(id=pk)
            if user.is_active == True:
                messages.info(request, user.first_name + ' ' +
                              user.last_name + ' is already now activated')
            else:
                user.is_active = True
                user.save()
                messages.success(request, user.first_name + ' ' +
                                 user.last_name + ' is now activated')
            deleted_accounts = []
            all_user = User.objects.all()
            for user in all_user:
                if not user.is_active:
                    deleted_accounts.append(user)

            context = {
                'deleted_accounts': deleted_accounts,
            }
            return render(request, 'Company/deleted_account.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')
# Manage Store


def view_store(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            all_store = Company_Store.objects.all()
            manager = Company_Store_Manager.objects.all()
            context = {
                'all_store': all_store,
                'manager': manager
            }
            return render(request, 'Company/store/store-view.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def add_store_company(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            if request.method == 'POST':
                Store_Name = request.POST['store_name']
                Address = request.POST['address']
                store = Company_Store.objects.create(
                    Store_Name=Store_Name, Address=Address)
                Product_Amount_in_Store.objects.create(store=store)

                messages.info(request, 'Store Successfully added')

                return redirect('view-store')
            else:
                return render(request, 'Company/store/add-store.html')
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def sore_ditel_view(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            manager = 'TBA'
            all_product = ProductNew.objects.all()
            store = Company_Store.objects.get(pk=pk)
            amount_store = Product_Amount_in_Store.objects.get(store=store)

            try:
                manager = Company_Store_Manager.objects.get(Store=store)
            except Company_Store_Manager.DoesNotExist:
                pass

            Total = 0
            Dopple = 'Dopple'

            table_data = {}
            for product in all_product:
                table_data[product.Product_Name] = getattr(
                    amount_store, product.Product_Name)
                Total += getattr(amount_store, product.Product_Name)

            context = {
                'all_product': all_product,
                'store': store,
                'amount': amount_store,
                'table_data': table_data,
                'Total': Total,
                'a': Dopple,
                'manager': manager,
            }
            return render(request, 'Company/store/store-detail.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')

# end Manage store

# Manage Region


def view_region(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            all_region = Region.objects.all()
            context = {
                'all_region': all_region,
            }
            return render(request, 'Company/region/region-view.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def add_region(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            if request.method == 'POST':
                region_name = request.POST.get('name')
                location = request.POST.get('location')
                address = request.POST.get('address')
                region = Region.objects.create(
                    Region_Name=region_name, Location=location,coverArea=address)
                if region:
                    messages.success(request, 'Region successfully Added')
                    return redirect('view-region')
                else:
                    message.error(request, 'Something went wrong')
                    context = {
                        'region_name': region_name,
                        'location': location,
                    }
                    return render(request, 'Company/region/add-region.html', context)

            return render(request, 'Company/region/add-region.html')
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')
def RegionDetail(request,pk):
    Searached_Region = Region.objects.get(id=pk)
    all_Agent=Agent.objects.filter(Region=Searached_Region)
    Total_Agent = all_Agent.count()
    agents=[]
    link ="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d170981.76251837067!2d39.00679496037457!3d8.550333049657196!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x164b1f65036ecb0f%3A0x6babded8f5e67ef6!2sAdama!5e0!3m2!1sen!2set!4v1667920771437!5m2!1sen!2set"
    for agent in all_Agent:
        agents.append(agent)
    total_Cust =0
    for agent in agents:
        all_cust=Customer.objects.filter(Agent=agent)
        total_Cust+=all_cust.count()
    context = {
          'region':Searached_Region,
          'all_Agent':all_Agent,
          'Total_Agent':Total_Agent,
          'Total_Customer':total_Cust,
          'link':link,
    }
    return render(request,'Company/region/regionDetail.html',context)
def RegionDelete(request,pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            b = pk
            Deleted_Region = Region.objects.get(id=pk)
            Region_Name = Deleted_Region.Region_Name
            all_region = Region.objects.all()
            context = {
                'all_region': all_region,
                'Region_Name': Region_Name,
                'b': b,
            }
            return render(request, 'Company/region/region-view.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')

def RegionDeleteComplet(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            all_region = Region.objects.all()
            if request.method == 'POST':
                a = request.POST.get('region_name')
                delete_region = Region.objects.get(id=a)
                Region_name = delete_region.Region_Name
                delete_region.delete()
                messages.success(request, 'successfull delete' + ' ' + Region_name)
                context = {
                    'all_region': all_region,
                    'a': a,
                    'product': product,
                    'name': a,
                }
                return render(request, 'Company/region/region-view.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')
    
# end Region


# Manage Product

def view_product(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':

            all_product = ProductNew.objects.all()
            context = {
                'all_product': all_product,
            }
            return render(request, 'Company/product/view-products.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def add_product(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            if request.method == 'POST':
                Product_Name = request.POST.get('product_name')
                img = request.FILES['add_image']
                Ag_by_Price_in_botle = request.POST.get('agby')
                Ag_se_Price_in_botle = request.POST.get('agse')
                cu_re_Price_in_botle = request.POST.get('cure')
                Ag_by_Price_in_crate=float(Ag_by_Price_in_botle)*24
                Ag_se_Price_in_crate=float(Ag_se_Price_in_botle)*24
                if Ag_by_Price_in_botle < Ag_se_Price_in_botle and Ag_se_Price_in_botle < cu_re_Price_in_botle:
                    ProductNew.objects.create(Product_Name=Product_Name, img=img,Price_in_botle_Agent_buy=Ag_by_Price_in_botle, Price_in_creates_Agent_buy=Ag_by_Price_in_crate,Price_in_botle_Agent_sell=Ag_se_Price_in_botle,Price_in_creates_Agent_sell=Ag_se_Price_in_crate,Price_in_botle_Custom_recom=cu_re_Price_in_botle)
                    Customer_order.add_to_class(product.Product_Name, models.IntegerField(default=0, null=True, blank=True))
                    messages.info(request, 'New Product Successfully added')
                    return redirect('view-product')
                else:
                    messages.error(request, 'The price input is incorrect')
                    return redirect('add-product')
            else:
                return render(request, 'Company/product/add-new-product.html')
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def product_update_pic_link(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            product = ProductNew.objects.get(id=pk)
            if request.method == 'POST':

                product.img = request.FILES['pic']
                product.save()

                messages.info(request, 'Product photo Successfully Updated')
                return redirect('view-product')
            context = {
                'product': product,
            }
            return render(request, 'Company/product/update_pic.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def update_product(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            product = ProductNew.objects.get(id=pk)
            if request.method == 'POST':
                product.Product_Name = request.POST['product_name']
                Ag_by_Price_in_botleN = request.POST.get('agby')
                product.Price_in_botle_Agent_buy=Ag_by_Price_in_botleN
                Ag_by_Price_in_crateN=float(Ag_by_Price_in_botleN)*24
                product.Price_in_creates_Agent_buy=Ag_by_Price_in_crateN
                Ag_se_Price_in_botleN = request.POST.get('agse')
                product.Price_in_botle_Agent_sell = Ag_se_Price_in_botleN
                Ag_se_Price_in_crateN=float(Ag_se_Price_in_botleN)*24
                product.Price_in_creates_Agent_sell=Ag_se_Price_in_crateN
                cu_re_Price_in_botleN = request.POST.get('csre')
                product.Price_in_botle_Custom_recom = cu_re_Price_in_botleN
                if Ag_by_Price_in_botleN < Ag_se_Price_in_botleN and Ag_se_Price_in_botleN < cu_re_Price_in_botleN:
                    product.save()
                    messages.info(request, 'Product Successfully Updated')
                    return redirect('view-product')
                else:
                    messages.error(request, 'The price input is incorrect')
                    return redirect('update-product',product.id)
            context = {
                'product': product,
            }
            return render(request, 'Company/product/update-product.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def delete_product_page(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            b = pk
            product = ProductNew.objects.get(id=pk)
            Product_Name = product.Product_Name
            all_product = ProductNew.objects.all()
            context = {
                'all_product': all_product,
                'Product_Name': Product_Name,
                'b': b,
            }

            return render(request, 'Company/product/view-products.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def delete_product(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':

            all_product = ProductNew.objects.all()
            if request.method == 'POST':
                a = request.POST.get('name')
                delete_product = ProductNew.objects.get(pk=a)
                name = delete_product.Product_Name
                delete_product.delete()
                messages.success(request, 'successfull delete' + ' ' + name)
                context = {
                    'all_product': all_product,
                    'a': a,
                    'product': product,
                    'name': a,

                }
                return render(request, 'Company/product/view-products.html', context)
            messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


# End Product


def advertisments_view(request):
    adds = Advertisment.objects.all()
    context = {'adds': adds}
    return render(request, 'Company/advertisments/advertisments.html', context)


def post_advertisment(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            adds = Advertisment.objects.all()

            context = {'adds': adds}
            if request.method == 'POST':
                product_namee = request.POST.get('product_name')
                product_photoe = request.FILES.get('product_photo')
                descriptione = request.POST.get('description')

                add = Advertisment.objects.create(
                    product_photo=product_photoe, product_price=65.2, product_name=product_namee, description=descriptione)

                if add:
                    return redirect('admin-dashbord')
                else:
                    return render(request, 'company/advertisments/advertisements.html', context)
            else:
                return render(request, 'company/advertisments/advertisements.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def add_ditel(request, pk):
    adds = Advertisment.objects.get(pk=pk)
    context = {
        'adds': adds,
    }
    return render(request, 'company/advertisments/ditel.html', context)


def delete_adds_post(request, pk):
    adds = Advertisment.objects.get(pk=pk)
    adds.delete()
    messages.success(request, 'Successfully remove Adevertasiment')
    return redirect('add-advertisments')


def product_in_store(request):
    all_Product_Amount_in_Store = Product_Amount_in_Store.objects.all()
    # p_a=Product_Amount_in_Store.objects.get(Store=1,Product_Name=2)
    all_Product = ProductNew.objects.all()
    all_Company_Store = Company_Store.objects.all()

    #  Name, id, produc_store, product_Quintitiy

#  store manager


#         price.append(product.Price_in_creates)
#         data=zip(prods,price,quantity,sub_total)
#         quantity.append(getattr(order,product.Product_Name))
#         sub_total.append(product.Price_in_creates*getattr(order,product.Product_Name))
#         grand_total+=float(product.Price_in_creates*getattr(order,product.Product_Name))
#         total_quantity+=(getattr(order,product.Product_Name))
#         VAT_Paid = float(grand_total * 0.15)

#     data=zip(prods,price,quantity,sub_total)

#     context={
#         'transaction':transaction,
#         'data':data,
#         'total_quantity':total_quantity,
#         'grand_total' :grand_total,
#         'VAT':VAT_Paid,

#     }
#     return render (request,'Company/store_manager/check_slip.html',context)

def store_manager_view(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':

            table_data = {}
            Total = 0
            arrimg = []
            arrvalu = []
            arrkey = []
            user = User.objects.get(id=request.user.id)
            all_Product = ProductNew.objects.all()

            try:
                company_manager = Company_Store_Manager.objects.get(user=user)
            except Exception as e:
                messages.error(request, 'permission denied ')
                return redirect('logout')

            spesific_store_from_manager = company_manager.Store
            store_id = spesific_store_from_manager.id
            spesific_store = Company_Store.objects.get(id=store_id)
            product_amount = Product_Amount_in_Store.objects.get(
                store=spesific_store)
            refile_product = add_to_store.objects.filter(
                Store=spesific_store).order_by('-date_created')
            for product in all_Product:
                arrimg.append(product.img)
                table_data[product.Product_Name] = (
                    (getattr(product_amount, product.Product_Name)))
                Total += getattr(product_amount, product.Product_Name)

            for key, valu in table_data.items():
                arrkey.append(key)
                arrvalu.append(valu)

            data = zip(arrkey, arrvalu, arrimg)

            context = {
                'table_data': table_data,
                'Total': Total,
                'data': data,
                'company_manager': company_manager,
                'spesific_store': spesific_store,
                'refile_product': refile_product,
            }

            return render(request, 'Company/store_manager/view-store.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def add_produc_to_store_view(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            all_Product = ProductNew.objects.all()
            user = User.objects.get(id=request.user.id)
            try:
                company_manager = Company_Store_Manager.objects.get(user=user)
            except Exception as e:
                messages.error(request, 'permission denied ')
                return redirect('logout')
            spesific_store_from_manager = company_manager.Store
            store_id = spesific_store_from_manager.id
            spesific_store = Company_Store.objects.get(id=store_id)
            product_amount = Product_Amount_in_Store.objects.get(
                store=spesific_store)

            name = ''
            if request.method == 'POST':
                name = request.POST['product']
                old_amount = getattr(product_amount, name)
                new_amount = request.POST['amount']
                update_amount = old_amount + int(new_amount)
                setattr(product_amount, name, update_amount)
                product_amount.save()
                add_to_store.objects.create(
                    Store=spesific_store, product=name, qunitiy=new_amount)
                messages.info(request, 'Store refilled successfully')
                return redirect('store-manager-home')

            context = {
                'all_Product': all_Product,


            }
            return render(request, 'Company/store_manager/add_to_store.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def aprove_order_view(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user = User.objects.get(id=request.user.id)
            try:
                company_manager = Company_Store_Manager.objects.get(user=user)
            except Exception as e:
                messages.error(request, 'permission denied ')
                return redirect('logout')
            spesific_store_from_manager = company_manager.Store
            store_id = spesific_store_from_manager.id
            spesific_store = Company_Store.objects.get(id=store_id)
            product_amount = Product_Amount_in_Store.objects.get(
                store=spesific_store)
            all_tranaction = []
            all_order_in_stor = Agent_order.objects.filter(
                Store=spesific_store)
            for order in all_order_in_stor:
                try:
                    Agent_Transaction.objects.get(Agent_order_id=order.id)
                except Exception as e:
                    continue
                all_tranaction.append(
                    Agent_Transaction.objects.get(Agent_order_id=order.id))

            context = {
                'all_tranaction': all_tranaction,

            }
            return render(request, 'Company/store_manager/approved_orders.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def approv_order(request):
    # the html file

    return render(request, 'Company/store_manager/approved_orders.html', context)


def stor_check_slip_view(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            transaction = Agent_Transaction.objects.get(id=pk)
            approve = Agent_Transaction.objects.get(id=pk)
            Agent_Name=approve.Agent_order_id.Agent.Full_Name
            Agent_Email=approve.Agent_order_id.Agent.user.email
            products = ProductNew.objects.all()
            order = Agent_order.objects.get(id=transaction.Agent_order_id.id)
            price = []
            prods = []
            quantity = []
            sub_total = []
            grand_total = 0
            VAT_Paid = 0.0
            total_quantity = 0
            for product in products:
                price.append(product. Price_in_creates_Agent_buy)
                prods.append(product.Product_Name)
                quantity.append(getattr(order, product.Product_Name))
                sub_total.append(product. Price_in_creates_Agent_buy *
                                 getattr(order, product.Product_Name))
                grand_total += float(product. Price_in_creates_Agent_buy *
                                     getattr(order, product.Product_Name))
                total_quantity += (getattr(order, product.Product_Name))
                VAT_Paid = float(grand_total * 0.15)

            data = zip(prods, price, quantity, sub_total)
            if request.method == 'POST':
                date1 = request.POST.get('date1')
                date2 = request.POST.get('date2')
                if date1 < date2:
                    transaction.scheduled_for = date1
                    transaction.scheduled_to = date2
                    subject = 'Order scheduled!'
                    message = 'Dear ' + Agent_Name + '\n' + 'Your Order has been scheduled successfully' + '\n'+'from The date '+ str(transaction.scheduled_for) + ' to ' + str(transaction.scheduled_to) + '\n' + 'Thank you for working with Us!'
                    to_email = Agent_Email
                    from_email = settings.EMAIL_HOST_USER
                    if subject and message and to_email and from_email:
                        try:
                            send_mail(subject, message, from_email,[to_email],fail_silently=False,)
                        except BadHeaderError:
                            return HttpResponse('Invalid header found.')
                    transaction.save()
                    
                   
                    # pls come and take it.
                    return redirect('view-aprove-order')
                else:
                    messages.error(
                        request, "Invalid schedule, please provide valid schedule")
            context = {
                'transaction': transaction,
                'data': data,
                'total_quantity': total_quantity,
                'grand_total': grand_total,
                'VAT': VAT_Paid,

            }
            return render(request, 'Company/store_manager/check_slip.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def allow_load_view(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':

            all_tranaction = Agent_Transaction.objects.all()
            context = {'all_tranaction': all_tranaction, }
            approve = Agent_Transaction.objects.get(id=pk)
            x = approve.Agent_order_id
            Or_id = x.id

            update_order = Agent_order.objects.get(id=Or_id)

            products = ProductNew.objects.all()

            user = User.objects.get(id=request.user.id)
            try:
                company_manager = Company_Store_Manager.objects.get(user=user)
            except Exception as e:
                messages.error(request, 'permission denied ')
                return redirect('logout')
            spesific_store_from_manager = company_manager.Store
            store_id = spesific_store_from_manager.id
            spesific_store = Company_Store.objects.get(id=store_id)
            product_amount = Product_Amount_in_Store.objects.get(
                store=spesific_store)

            print('*******************')
            for product in products:
                name = ''

                name = product.Product_Name
                old_amount = getattr(product_amount, str(name))
                new_amount = getattr(update_order, name)
                if new_amount > old_amount:
                    messages.info(request, 'Product in Store not sufficent')
                    return render(request, 'Company/store_manager/approved_orders.html', context)

                else:

                    update_amount = old_amount - int(new_amount)
                    setattr(product_amount, name, update_amount)
                    product_amount.save()
                    update_order.status = 'Recived'
                    update_order.save()
                    add_to_store.objects.create(
                        Store=spesific_store, product=name, qunitiy=new_amount)
                    messages.info(request, 'successful')

            return render(request, 'Company/store_manager/approved_orders.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def loaded_order(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':

            all_tranaction = Agent_Transaction.objects.all()

            context = {
                'all_tranaction': all_tranaction,

            }
            return render(request, 'Company/store_manager/loaded.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')
# END store manager


# Report
def view_report(request):
    all_tran = Agent_Transaction.objects.all()
    context = {
        'all_tran': all_tran,
    }
    return render(request, 'Company/report/generate-report.html', context)
def storeRefillReport(request):
    RecentRefill = add_to_store.objects.all().order_by('-date_created')
    context = {
        'RecentRefill':RecentRefill
    }
    
    return render(request,'Company/report/StoreRefill.html',context )
# END Report

#  Finance admin


def finance_admin_view(request):
    try:
        if request.user.groups.all()[0].name == 'Financ_admin':
            
            all_tranaction = Agent_Transaction.objects.all()
            new_order=[]
            for tran in all_tranaction:
                new_order.append(tran.Agent_order_id)
           
            approv_order = 0
            Pending_order = 0
            Rejected_order = 0
            
            for order in new_order:
                if order.status == 'Approved':
                    approv_order +=1  
                elif order.status == 'Pending':
                    Pending_order +=1
                elif order.status == 'Reject':
                    Rejected_order +=1   
            # for tran in all_tranaction:
           
            context = {
                'all_tranaction': all_tranaction,
                'approv_order':approv_order,
                'Pending_order':Pending_order,
                'Rejected_order':Rejected_order,
            }
            return render(request, 'Company/finance/home.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')

def aprove_order_history_view(request):
    try:
        if request.user.groups.all()[0].name == 'Financ_admin':
            all_tranaction = Agent_Transaction.objects.all()
            new_order=[]
            for tran in all_tranaction:
                new_order.append(tran.Agent_order_id)
            approv_order = 0
            Pending_order = 0
            Rejected_order = 0
            for order in new_order:
                if order.status == 'Approved':
                    approv_order +=1
                elif order.status == 'Pending':
                    Pending_order +=1
                elif order.status == 'Reject':
                    Rejected_order +=1
            # for tran in all_tranaction:
            
            context = {
                'all_tranaction': all_tranaction,
                'approv_order':approv_order,
                'Pending_order':Pending_order,
                'Rejected_order':Rejected_order,
            }
            return render(request, 'Company/finance/approved-orders-history.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def Reject_order_list(request):
    try:
        if request.user.groups.all()[0].name == 'Financ_admin':
            all_tranaction = Agent_Transaction.objects.all()
            new_order=[]
            for tran in all_tranaction:
                new_order.append(tran.Agent_order_id)
            approv_order = 0
            Pending_order = 0
            Rejected_order = 0
            for order in new_order:
                if order.status == 'Approved':
                    approv_order +=1
                elif order.status == 'Pending':
                    Pending_order +=1
                elif order.status == 'Reject':
                    Rejected_order +=1
            # for tran in all_tranaction:
            
            context = {
                'all_tranaction': all_tranaction,
                'approv_order':approv_order,
                'Pending_order':Pending_order,
                'Rejected_order':Rejected_order,
            }
            return render(request, 'Company/finance/rejected.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def reject_order(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Financ_admin':
            all_tranaction = Agent_Transaction.objects.all()
            approve = Agent_Transaction.objects.get(id=pk)
            x = approve.Agent_order_id
            oa=Agent_order.objects.get(id=x.id)
            print("-----i dont ----")
            print(oa)
            print("---------")
            Or_id = x.id
            update_order = Agent_order.objects.get(id=Or_id)
            if update_order.status == 'Approved':
                    messages.info(request, 'You can not reject order once it is approved.')
                    return redirect('finance_admin_home')
            elif update_order.status != 'Reject':
                update_order.status = 'Reject'
                update_order.save()
                
                messages.success(request, 'The order has been Rejected successfully.')
                return redirect('finance_admin_home')
        
            
            else:
                messages.info(request, 'The order has already been Rejected.')
                return redirect('finance_admin_home')

            # Email message 
            # hello Ms Agent 
            # Your Order sucessfully approved by fadmin
            # Order Code :
            # soonly you will be sechduled from store 

            context = {
                'all_tranaction': all_tranaction,
            }
            return render(request, 'Company/finance/home.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def unapproves_Order(request):
    try:
        if request.user.groups.all()[0].name == 'Financ_admin':
            all_tranaction = Agent_Transaction.objects.all()
            new_order=[]
            for tran in all_tranaction:
                new_order.append(tran.Agent_order_id)
            approv_order = 0
            Pending_order = 0
            Rejected_order =0
            for order in new_order:
                if order.status == 'Approved':
                    approv_order +=1
                elif order.status == 'Pending':
                    Pending_order +=1
                elif order.status == 'Reject':
                    Rejected_order +=1
            # for tran in all_tranaction:
            
            context = {
                'all_tranaction': all_tranaction,
                'approv_order':approv_order,
                'Pending_order':Pending_order,
                'Rejected_order':Rejected_order
            }
            return render(request, 'Company/finance/unapproved_Order.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')

# 
def check_slip_view(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Financ_admin':
            transaction = Agent_Transaction.objects.get(id=pk)
            products = ProductNew.objects.all()
            order = Agent_order.objects.get(id=transaction.Agent_order_id.id)
            price = []
            prods = []
            quantity = []
            sub_total = []
            grand_total = 0
            VAT_Paid = 0.0
            total_quantity = 0
            for product in products:
                price.append(product. Price_in_creates_Agent_buy)
                prods.append(product.Product_Name)
                quantity.append(getattr(order, product.Product_Name))
                sub_total.append(product.Price_in_creates_Agent_buy *
                                 getattr(order, product.Product_Name))
                grand_total += float(product.Price_in_creates_Agent_buy *
                                     getattr(order, product.Product_Name))
                total_quantity += (getattr(order, product.Product_Name))
                VAT_Paid = float(grand_total * 0.15)

            data = zip(prods, price, quantity, sub_total)

            context = {
                'transaction': transaction,
                'data': data,
                'total_quantity': total_quantity,
                'grand_total': grand_total,
                'VAT': VAT_Paid,
}
            return render(request, 'Company/finance/new_order-details.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def approve_view(request, pk):
    try:
        if request.user.groups.all()[0].name == 'Financ_admin':
            all_tranaction = Agent_Transaction.objects.all()
            approve = Agent_Transaction.objects.get(id=pk)
            Agent_Name=approve.Agent_order_id.Agent.Full_Name
            Agent_Email=approve.Agent_order_id.Agent.user.email
            print(Agent_Name)
            print(Agent_Email)
            x = approve.Agent_order_id
            oa=Agent_order.objects.get(id=x.id)
            print("-----i dont ----")
            print(oa)
            print("---------")
# ////////////////////////////////////////////////////////////////
            transaction = Agent_Transaction.objects.get(id=pk)
            print("Your order history")
            print(transaction.TransactionCode)
            print(transaction.Agent_order_id.Store.Store_Name)
            print("yenePay")
            print(transaction.Total_Amount)
                
# //////////////////////////////////////////////////////////////////

            Or_id = x.id
            update_order = Agent_order.objects.get(id=Or_id)
            if update_order.status != 'Approved':
                update_order.status = 'Approved'
                update_order.save()
                messages.success(request, 'The order has been approved successfully.')
                store_id=transaction.Agent_order_id.Store.id
                store_manager=Company_Store_Manager.objects.get(Store=store_id)
               
                store_manager_email=(store_manager.user.email)
                
                subject = 'Order Approved!'
                message = 'Dear Store Manager' + '\n' + 'We have approved this order, and please schedule it as soon as possible.' + '\n'+'The order history'+'\n'+'TransactionCode: '+transaction.TransactionCode +'\n' 'From Store: '+transaction.Agent_order_id.Store.Store_Name + '\n' 'Date: '+  str(datetime.datetime.now()) + '\n' 'Payed Amount: ' + str(transaction.Total_Amount) + '\n' 'payement through: '+ 'yenpay'+ '\n'  +'Thank you working with us!' 
                to_email = store_manager_email
                from_email = settings.EMAIL_HOST_USER
                if subject and message and to_email and from_email:
                    try:
                        send_mail(subject, message, from_email,[to_email],fail_silently=False,)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                

                subject = 'Order Approved!'
                message = 'Dear' + Agent_Name + '\n' + 'Your Order has been approved successfully' + '\n'+'The order history'+'\n'+'TransactionCode: '+transaction.TransactionCode +'\n' 'From Store: '+transaction.Agent_order_id.Store.Store_Name + '\n' 'Date: '+  str(datetime.datetime.now()) + '\n' 'Payed Amount: ' + str(transaction.Total_Amount) + '\n' 'payement through: '+ 'yenpay'+ '\n'  +'Thank you working with us!' 
                print(message)
                to_email = Agent_Email
                from_email = settings.EMAIL_HOST_USER
                if subject and message and to_email and from_email:
                    try:
                        send_mail(subject, message, from_email,[to_email],fail_silently=False,)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                return redirect('finance_admin_home')
                
                # ///////
            else:
                messages.info(request, 'The order has already been approved.')
                return redirect('finance_admin_home')
            # Email message 
            # hello Ms Agent 
            # Your Order sucessfully approved by fadmin
            # Order Code :
            # soonly you will be sechduled from store 
            context = {
                'all_tranaction': all_tranaction,
            }
            return render(request, 'Company/finance/home.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')


def check_store_view(request):
    return render(request, 'Company/finance/check-store.html', {})


def show_profile_finance(request):
    try:
        if request.user.groups.all()[0].name == 'Financ_admin':
            users = User.objects.get(id=request.user.id)

            admin = Finance_Manager.objects.get(user=users)
            print(admin)
            context = {
                'admin': admin,
            }
            return render(request, 'Company/finance/profile/show_profile_finance.html', context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')




# END Finance admin
# Send Message
def send_message(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        to_email = request.POST.get('to_email', '')
        from_email = settings.EMAIL_HOST_USER
        send = False
        if subject and message and to_email and from_email:
            try:
                send_mail(subject, message, from_email,[to_email],fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            send = True
            context = {
                'send':send,
            }
            return render(request, 'Company/send-message.html',context)
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return render(request, 'Company/send-message.html', {})

    return render(request, 'Company/send-message.html', {})

def myaccount(request):
    try:
        if request.user.groups.all()[0].name == 'Admin':
            my_Account=yenePay.objects.all()
            MId=my_Account[0].MerchantId
            if request.method=='POST':
                new_id=request.POST.get('new_mid')
                old_id=request.POST.get('old_mid')
                if old_id == new_id:
                    messages.error(request,'previous merchant id and newer merchant id is the same ! ')
                    return redirect('myaccount')
                else:
                    merchant_id=yenePay.objects.get(MerchantId=old_id)
                    merchant_id.MerchantId=new_id
                    merchant_id.save()
                    messages.success(request,'you have successfully updated your merchant id!')
                    return redirect('myaccount')
            context = {
                'my_Account':my_Account,
                'MId':MId,
            }
            print(my_Account[0].username)
            
            return render(request, 'Company/my_account.html',context)
        messages.error(request, 'permission denied ')
        return redirect('logout')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('logout')

def new_examlpe(request):
    return render(request,'Company/example.html')