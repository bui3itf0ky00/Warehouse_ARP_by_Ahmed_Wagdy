# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.generic.edit import UpdateView
from app.forms import AddCompanyForm, AddFarmForm, AddJobForm, AddWorkerForm, AddSupplierForm, AddClientForm, \
    AddProductForm, WarehouseEntryForm, FundsTransfaerForm, AddDailyForm, PickOstazForm, AddCategoryForm, \
    ActivationForm, \
    AddBuyInvoice, AddSellInvoice, FarmReportForm, SellInvoiceFilterForm, CreateUserForm, RequestActivationForm, \
    BuyInvoiceFilterForm, NewDailyForm, CreateTalabForm, TalabatDoForm, IncomeListFilterForm, DailyReportFilterForm, \
    SafeDepositForm, SafecostsForm, ClientPayForm
from app.models import Company, Farm, Job, Worker, Supplier, Client, Warehouse, Product, Balance, Daily, Type, Category, \
    SellInvoice, BuyInvoice, Talabat, Mezan, Account, Activation
from datetime import date, datetime
from django.core.management import call_command
import random
import datetime
from django.core.mail import send_mail, EmailMessage


def activation_request(request):
    request_activation_form = RequestActivationForm(request.POST)
    if request.method == 'POST':
        if request_activation_form.is_valid():
            serial_obj = Activation.objects.filter()[0]
            serial = serial_obj.serial1
            mobile = request_activation_form.cleaned_data['mobile_number']
            email_msg = 'serial : "' + serial + '" - mobile: ' + mobile
            email = EmailMessage('serial request ', email_msg, to=['ahmed.w.amin@gmail.com'])
            email.send()
            return redirect('serial_request_done')
    else:
        request_activation_form = RequestActivationForm(request.POST)
    context = {
        'request_activation_form': request_activation_form,
    }
    return render(request, 'activate/request.html', context)


def activation(request):
    activation_form = ActivationForm(request.POST)
    if request.method == 'POST':
        if activation_form.is_valid():
            current_seial_obj = Activation.objects.filter()[0]
            current_seial = current_seial_obj.serial1
            new_serial = activation_form.cleaned_data['serial']
            new_company = activation_form.cleaned_data['company_name']
            if current_seial == new_serial:
                call_command('clear_models')
                current_seial_obj.is_active = True
                current_seial_obj.company = new_company
                current_seial_obj.save()
                company_obj = Company.objects.filter()[0]
                company_obj.company_name = new_company
                company_obj.save()
                new_farm = Farm(farm_name=company_obj)
                new_farm.save()
                new_balance = Balance(farm=new_farm, balance=0)
                new_balance.save()
                return redirect('index')
            else:
                pass
    else:
        activation_form = ActivationForm(request.POST)
    context = {
        'activation_form': activation_form,
    }
    return render(request, 'activate/activate.html', context)


def serial_request_done(request):
    return render(request, 'activate/request_done.html')


def user_create(request):
    all_users = Account.objects.all()
    create_user_form = CreateUserForm(request.POST)
    if request.method == 'POST':
        if create_user_form.is_valid():
            username = create_user_form.cleaned_data['username']
            password = create_user_form.cleaned_data['password']
            role = create_user_form.cleaned_data['role']
            new_user = User(username=username)
            new_user.set_password(password)
            new_user.save()
            new_account = Account(user=new_user, role=role)
            new_account.save()
            return redirect('user_create')
    else:
        create_user_form = CreateUserForm(request.POST)
    context = {
        'create_user_form': create_user_form,
        'all_users': all_users,
    }
    return render(request, 'users/create.html', context)


def user_delete(request, pk):
    current_user = get_object_or_404(User, pk=pk)
    current_account = Account.objects.get(user=current_user)
    current_account.delete()
    current_user.delete()
    return redirect('user_create')


@login_required
def index(request):
    check_activation = Activation.objects.filter()
    if check_activation.count() == 0:
        serial = random.randint(111111111111111111, 99999999999999999999999999999999999999)
        company = 'Zoom Print'
        today = datetime.datetime.now()
        add = Activation(serial1=serial, company=company, last_time=today)
        add.save()
    else:
        my_company = check_activation[0].company
        type_list = ['الاصول الثابتة', 'الاصول المتداولة ', 'الخصوم المتدوالة', 'الخصوم غير المتداولة', 'حقوق الملكية',
                     'المصروفات', 'الإيرادات']
        current_company = Company.objects.filter()
        current_types = Type.objects.filter()
        current_category = Category.objects.filter()
        if current_company.count() == 0:
            add_company = Company(company_name=my_company)
            add_company.save()
            new_farm = Farm(farm_name=my_company)
            new_farm.save()
            new_balance = Balance(farm=new_farm, balance=0)
            new_balance.save()
        else:
            pass
        if current_types.count() == 0:
            for item in type_list:
                add_type = Type(type_name=item)
                add_type.save()
        else:
            pass
        if current_category.count() == 0:
            naqdya_type = Type.objects.get(type_name='الاصول المتداولة ')
            naqdya = Category(category_name="النقدية", type=naqdya_type)
            naqdya.save()
            naqdya_mezan = Mezan(name=naqdya)
            naqdya_mezan.save()
            benook_type = Type.objects.get(type_name='الاصول المتداولة ')
            benook = Category(category_name="البنوك", type=naqdya_type)
            benook.save()
            benook_mezan = Mezan(name=benook)
            benook_mezan.save()
            gary_type = Type.objects.get(type_name='الاصول المتداولة ')
            gary = Category(category_name="جارى شركات شقيقة", type=naqdya_type)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            gary_type = Type.objects.get(type_name='الاصول المتداولة ')
            gary = Category(category_name="العملاء", type=naqdya_type)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            gary_type = Type.objects.get(type_name='الاصول المتداولة ')
            gary = Category(category_name="مصروف مقدم", type=naqdya_type)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            gary_type = Type.objects.get(type_name='الاصول المتداولة ')
            gary = Category(category_name="الخزنه الرئيسيه", type=naqdya_type)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            gary_type = Type.objects.get(type_name='الاصول المتداولة ')
            gary = Category(category_name="العهد", type=naqdya_type)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            gary_type = Type.objects.get(type_name='الاصول المتداولة ')
            gary = Category(category_name="السلف", type=naqdya_type)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type2 = Type.objects.get(type_name='الاصول الثابتة')
            gary = Category(category_name="صافى الأصول الثابتة - تكلفة", type=type2)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type2 = Type.objects.get(type_name='الاصول الثابتة')
            gary = Category(category_name="جارى الفروع المدينة", type=type2)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type3 = Type.objects.get(type_name='الخصوم المتدوالة')
            gary = Category(category_name='الموردون', type=type3)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type3 = Type.objects.get(type_name='الخصوم المتدوالة')
            gary = Category(category_name='اوراق دفع', type=type3)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type3 = Type.objects.get(type_name='الخصوم المتدوالة')
            gary = Category(category_name='مصروفات مستحقة', type=type3)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type3 = Type.objects.get(type_name='الخصوم المتدوالة')
            gary = Category(category_name='تأمينات وأمانات للغير', type=type3)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type4 = Type.objects.get(type_name='الخصوم غير المتداولة')
            gary = Category(category_name='مخصص مستحقات العاملين', type=type4)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type4 = Type.objects.get(type_name='الخصوم غير المتداولة')
            gary = Category(category_name='جارى الفروع الدائنة', type=type4)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type5 = Type.objects.get(type_name='حقوق الملكية')
            gary = Category(category_name='رأس المال', type=type5)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
            type5 = Type.objects.get(type_name='حقوق الملكية')
            gary = Category(category_name='جارى صاحب المؤسسة', type=type5)
            gary.save()
            gary_mezan = Mezan(name=gary)
            gary_mezan.save()
        else:
            pass
    all_farms = Farm.objects.all()
    all_workers = Worker.objects.all()
    all_balance = Balance.objects.all()
    total_balance = []
    for item in all_balance:
        total_balance.append(item.balance)
    final_total_balance = sum(total_balance)
    all_buy_invoices = BuyInvoice.objects.all()
    all_sell_invoices = SellInvoice.objects.all()
    company = Company.objects.filter()[0]
    context = {
        'all_farms': all_farms,
        'all_workers': all_workers,
        'final_total_balance': final_total_balance,
        'all_buy_invoices': all_buy_invoices,
        'all_sell_invoices': all_sell_invoices,
        'company': company,
    }
    return render(request, 'app/index.html', context)


@login_required
def workers(request):
    all_workers = Worker.objects.filter(worker_deleted=False)
    context = {
        'all_workers': all_workers,
    }
    return render(request, 'app/workers.html', context)


@login_required
def nocomp(request):
    return render(request, 'app/nocomp.html')


@login_required
def add_company(request):
    add_company_form = AddCompanyForm(request.POST)
    if request.method == 'POST':
        if add_company_form.is_valid():
            add_company_form.save()
            return redirect('index')
    else:
        add_company_form = AddCompanyForm()

    context = {
        'add_company_form': add_company_form,
    }

    return render(request, 'app/add_company.html', context)


@login_required
def add_farm(request):
    add_farm_form = AddFarmForm(request.POST)
    if request.method == 'POST':
        if add_farm_form.is_valid():
            ad_farm = add_farm_form.save(commit=False)
            ad_farm.save()
            add_balance = Balance(farm=ad_farm, balance=0)
            add_balance.save()
            return redirect('index')
    else:
        add_farm_form = AddFarmForm()

    context = {
        'add_farm_form': add_farm_form,
    }
    return render(request, 'app/add_farm.html', context)


@login_required
def farm_details(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    farm_workers = Worker.objects.filter(worker_farm=current_farm, worker_deleted=False)
    context = {
        'current_farm': current_farm,
        'farm_workers': farm_workers,
    }
    return render(request, 'app/farm_details.html', context)


@login_required
def farm_delete(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    current_farm.delete()
    return redirect('index')


class FarmUpdate(UpdateView):
    model = Farm
    fields = ['farm_name']
    template_name_suffix = '_update_form'


@login_required
def workers_add(request):
    add_worker_form = AddWorkerForm(request.POST)
    if request.method == 'POST':
        if add_worker_form.is_valid():
            add_worker_form.save()
            return redirect('workers')
    else:
        add_worker_form = AddWorkerForm()
    context = {
        'add_worker_form': add_worker_form,
    }

    return render(request, 'app/workers_add.html', context)


@login_required
def jobs_add(request):
    add_job_form = AddJobForm(request.POST)
    all_jobs = Job.objects.all()
    if request.method == 'POST':
        if add_job_form.is_valid():
            ad_job = add_job_form.save(commit=False)
            ad_job.save()
            return redirect('jobs_add')
    else:
        add_job_form = AddJobForm()

    context = {
        'add_job_form': add_job_form,
        'all_jobs': all_jobs,
    }

    return render(request, 'app/jobs_add.html', context)


@login_required
def job_delete(request, pk):
    current_job = get_object_or_404(Job, pk=pk)
    current_job.delete()
    return redirect('jobs_add')


class JobUpdate(UpdateView):
    model = Job
    fields = ['job_name']
    template_name_suffix = '_update_form'


@login_required
def worker_details(request, pk):
    current_worker = get_object_or_404(Worker, pk=pk)
    context = {
        'current_worker': current_worker,
    }
    return render(request, 'app/worker_details.html', context)


@login_required
def worker_delete(request, pk):
    current_worker = get_object_or_404(Worker, pk=pk)
    current_worker.delete()
    return redirect('workers')


class WorkerUpdate(UpdateView):
    model = Worker
    fields = ['worker_name', 'worker_phone', 'worker_id', 'worker_address', 'worker_job', 'worker_farm',
              'worker_salary', 'worker_work_date', 'worker_image']
    template_name_suffix = '_update_form'


@login_required
def worker_archive(request, pk):
    current_worker = get_object_or_404(Worker, pk=pk)
    current_worker.worker_end_time = date.today()
    current_worker.worker_deleted = True
    current_worker.save()
    return redirect('workers')


@login_required
def old_workers(request):
    old_worker = Worker.objects.filter(worker_deleted=True)
    context = {
        'old_worker': old_worker,
    }
    return render(request, 'app/old_workers.html', context)


@login_required
def supplier(request):
    all_supply = Supplier.objects.all()
    context = {
        'all_supply': all_supply,
    }
    return render(request, 'app/supplier.html', context)


@login_required
def supplier_add(request):
    add_supplier_form = AddSupplierForm(request.POST)
    if request.method == 'POST':
        if add_supplier_form.is_valid():
            add_supplier_form.save()
            return redirect('supplier')
    else:
        add_supplier_form = AddSupplierForm()
    context = {
        'add_supplier_form': add_supplier_form,
    }
    return render(request, 'app/add_supplier.html', context)


@login_required
def clients(request):
    all_clients = Client.objects.all()
    context = {
        'all_clients': all_clients,
    }
    return render(request, 'app/clients.html', context)


@login_required
def clients_add(request):
    add_client_form = AddClientForm(request.POST)
    if request.method == 'POST':
        if add_client_form.is_valid():
            add_client_form.save()
            return redirect('clients')
    else:
        add_client_form = AddClientForm()
    context = {
        'add_client_form': add_client_form,
    }
    return render(request, 'app/clients_add.html', context)


@login_required
def supplier_delete(request, pk):
    current_supply = get_object_or_404(Supplier, pk=pk)
    current_supply.delete()
    return redirect('supplier')


class SupplierUpdate(UpdateView):
    model = Supplier
    fields = ['supplier_name', 'supplier_ID_number']
    template_name_suffix = '_update_form'


@login_required
def supplier_details(request, pk):
    current_supply = get_object_or_404(Supplier, pk=pk)
    context = {
        'current_supply': current_supply,
    }
    return render(request, 'app/supplier_details.html', context)


@login_required
def client_details(request, pk):
    current_client = get_object_or_404(Client, pk=pk)
    context = {
        'current_client': current_client,
    }
    return render(request, 'app/client_details.html', context)


@login_required
def client_ta7sel(request, pk):
    current_client = get_object_or_404(Client, pk=pk)
    client_pay_form = ClientPayForm(request.POST)
    farm_obj = Farm.objects.all()[0]
    if request.method == 'POST':
        if client_pay_form.is_valid():
            amount = client_pay_form.cleaned_data['amount']
            current_client_balance = current_client.client_balance
            removed_balance = amount
            new_balance = int(current_client_balance) - int(removed_balance)
            current_client.client_balance = new_balance
            current_client.save()
            new_daily = Daily(text='تحصيل من العميل ' + current_client.client_name, da2en=amount, paid=amount,
                              unpaid=0, farm=farm_obj)
            new_daily.save()
            balance_obj = Balance.objects.get(farm=farm_obj)
            old_balance = balance_obj.balance
            added_balance = amount
            new_balance = int(old_balance) + int(added_balance)
            balance_obj.balance = new_balance
            balance_obj.save()
            return redirect('client_details', current_client.pk)
    else:
        client_pay_form = ClientPayForm(request.POST)
    context = {
        'current_client': current_client,
        'client_pay_form': client_pay_form,
    }
    return render(request, 'app/client_ta7sel.html', context)


@login_required
def client_delete(request, pk):
    current_client = get_object_or_404(Client, pk=pk)
    current_client.delete()
    return redirect('clients')


class ClientUpdate(UpdateView):
    model = Client
    fields = ['client_name', 'client_ID_number']
    template_name_suffix = '_update_form'


@login_required
def warehouse(request):
    all_warehouse = Warehouse.objects.all()
    context = {
        'all_warehouse': all_warehouse,
    }
    return render(request, 'app/warehouse.html', context)


@login_required
def product(request):
    all_products = Product.objects.all()
    context = {
        'all_products': all_products,
    }
    return render(request, 'app/product.html', context)


@login_required
def product_add(request):
    add_product_form = AddProductForm(request.POST)
    if request.method == 'POST':
        if add_product_form.is_valid():
            add_product_form.save()
            return redirect('product')
    else:
        add_product_form = AddProductForm()
    context = {
        'add_product_form': add_product_form,
    }
    return render(request, 'app/product_add.html', context)


@login_required
def product_details(request, pk):
    current_product = get_object_or_404(Product, pk=pk)
    context = {
        'current_product': current_product,
    }
    return render(request, 'app/product_details.html', context)


@login_required
def product_delete(request, pk):
    current_product = get_object_or_404(Product, pk=pk)
    current_product.delete()
    return redirect('product')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['product_name']
    template_name_suffix = '_update_form'


@login_required
def warehouse_entry(request):
    warehouse_entry_form = WarehouseEntryForm(request.POST)
    if request.method == 'POST':
        if warehouse_entry_form.is_valid():
            ada_entry = warehouse_entry_form.save(commit=False)
            current = Warehouse.objects.filter(item_name=ada_entry.item_name)
            if current:
                current1 = current[0]
                current2 = current1.item_quantity
                current3 = current2 + ada_entry.item_quantity
                current1.item_quantity = current3
                current1.save()
                return redirect('warehouse')
            else:
                ada_entry.save()
                return redirect('warehouse')
    else:
        warehouse_entry_form = WarehouseEntryForm()
    context = {
        'warehouse_entry_form': warehouse_entry_form,
    }
    return render(request, 'app/warehouse_entry.html', context)


@login_required
def warehouse_out(request, pk):
    current_item = get_object_or_404(Warehouse, pk=pk)
    quantity = request.POST.get('out_number')
    current = current_item.item_quantity
    if request.method == 'POST':
        new = int(current) - int(quantity)
        current_item.item_quantity = new
        current_item.save()
        return redirect('warehouse')
    context = {
        'current_item': current_item,
        'current': current,
    }
    return render(request, 'app/item_out.html', context)


@login_required
def finance_daily(request):
    all_daily = Daily.objects.all().order_by('-date')
    context = {
        'all_daily': all_daily,
    }
    return render(request, 'app/finance_daily.html', context)


@login_required
def ostaz(request):
    pick_ostaz_form = PickOstazForm(request.POST)
    if request.method == 'POST':
        if pick_ostaz_form.is_valid():
            current_type = pick_ostaz_form.cleaned_data['category']
            return redirect('ostaz_details', pk=current_type.pk)
    else:
        pick_ostaz_form = PickOstazForm()
    context = {
        'pick_ostaz_form': pick_ostaz_form,
    }
    return render(request, 'ostaz.html', context)


@login_required
def ostaz_details(request, pk):
    current_category = get_object_or_404(Category, pk=pk)
    pick_ostaz_form = PickOstazForm(request.POST)
    all_current_da2n = Daily.objects.filter(da2en_from_cat=current_category)
    all_current_maden = Daily.objects.filter(maden_from_cat=current_category)
    jan_maden = []
    feb_maden = []
    march_maden = []
    april_maden = []
    may_maden = []
    june_maden = []
    july_maden = []
    aug_maden = []
    sep_maden = []
    oct_maden = []
    nov_maden = []
    dec_maden = []
    jan_da2en = []
    feb_da2en = []
    march_da2en = []
    april_da2en = []
    may_da2en = []
    june_da2en = []
    july_da2en = []
    aug_da2en = []
    sep_da2en = []
    oct_da2en = []
    nov_da2en = []
    dec_da2en = []
    for item in all_current_da2n:
        if item.date.month == 1:
            jan_da2en.append(item.da2en)
    final_1_da2en = sum(jan_da2en)
    for item in all_current_da2n:
        if item.date.month == 2:
            feb_da2en.append(item.da2en)
    final_2_da2en = sum(feb_da2en)
    for item in all_current_da2n:
        if item.date.month == 3:
            march_da2en.append(item.da2en)
    final_3_da2en = sum(march_da2en)
    for item in all_current_da2n:
        if item.date.month == 4:
            april_da2en.append(item.da2en)
    final_4_da2en = sum(april_da2en)
    for item in all_current_da2n:
        if item.date.month == 5:
            may_da2en.append(item.da2en)
    final_5_da2en = sum(may_da2en)
    for item in all_current_da2n:
        if item.date.month == 6:
            june_da2en.append(item.da2en)
    final_6_da2en = sum(june_da2en)
    for item in all_current_da2n:
        if item.date.month == 7:
            july_da2en.append(item.da2en)
    final_7_da2en = sum(july_da2en)
    for item in all_current_da2n:
        if item.date.month == 8:
            aug_da2en.append(item.da2en)
    final_8_da2en = sum(aug_da2en)
    for item in all_current_da2n:
        if item.date.month == 9:
            sep_da2en.append(item.da2en)
    final_9_da2en = sum(sep_da2en)
    for item in all_current_da2n:
        if item.date.month == 10:
            oct_da2en.append(item.da2en)
    final_10_da2en = sum(oct_da2en)
    for item in all_current_da2n:
        if item.date.month == 11:
            nov_da2en.append(item.da2en)
    final_11_da2en = sum(nov_da2en)
    for item in all_current_da2n:
        if item.date.month == 12:
            dec_da2en.append(item.da2en)
    final_12_da2en = sum(dec_da2en)
    for item in all_current_maden:
        if item.date.month == 1:
            jan_maden.append(item.maden)
    final_1_maden = sum(jan_maden)
    for item in all_current_maden:
        if item.date.month == 2:
            feb_maden.append(item.maden)
    final_2_maden = sum(feb_maden)
    for item in all_current_maden:
        if item.date.month == 3:
            march_maden.append(item.maden)
    final_3_maden = sum(march_maden)
    for item in all_current_maden:
        if item.date.month == 4:
            april_maden.append(item.maden)
    final_4_maden = sum(april_maden)
    for item in all_current_maden:
        if item.date.month == 5:
            may_maden.append(item.maden)
    final_5_maden = sum(may_maden)
    for item in all_current_maden:
        if item.date.month == 6:
            june_maden.append(item.maden)
    final_6_maden = sum(june_maden)
    for item in all_current_maden:
        if item.date.month == 7:
            july_maden.append(item.maden)
    final_7_maden = sum(july_maden)
    for item in all_current_maden:
        if item.date.month == 8:
            aug_maden.append(item.maden)
    final_8_maden = sum(aug_maden)
    for item in all_current_maden:
        if item.date.month == 9:
            sep_maden.append(item.maden)
    final_9_maden = sum(sep_maden)
    for item in all_current_maden:
        if item.date.month == 10:
            oct_maden.append(item.maden)
    final_10_maden = sum(oct_maden)
    for item in all_current_maden:
        if item.date.month == 11:
            nov_maden.append(item.maden)
    final_11_maden = sum(nov_maden)
    for item in all_current_maden:
        if item.date.month == 12:
            dec_maden.append(item.maden)
    final_12_maden = sum(dec_maden)
    if request.method == 'POST':
        if pick_ostaz_form.is_valid():
            current_category = pick_ostaz_form.cleaned_data['category']
            return redirect('ostaz_details', pk=current_category.pk)
    else:
        pick_ostaz_form = PickOstazForm()
    context = {
        'current_category': current_category,
        'pick_ostaz_form': pick_ostaz_form,
        'final_1_da2en': final_1_da2en,
        'final_2_da2en': final_2_da2en,
        'final_3_da2en': final_3_da2en,
        'final_4_da2en': final_4_da2en,
        'final_5_da2en': final_5_da2en,
        'final_6_da2en': final_6_da2en,
        'final_7_da2en': final_7_da2en,
        'final_8_da2en': final_8_da2en,
        'final_9_da2en': final_9_da2en,
        'final_10_da2en': final_10_da2en,
        'final_11_da2en': final_11_da2en,
        'final_12_da2en': final_12_da2en,
        'final_1_maden': final_1_maden,
        'final_2_maden': final_2_maden,
        'final_3_maden': final_3_maden,
        'final_4_maden': final_4_maden,
        'final_5_maden': final_5_maden,
        'final_6_maden': final_6_maden,
        'final_7_maden': final_7_maden,
        'final_8_maden': final_8_maden,
        'final_9_maden': final_9_maden,
        'final_10_maden': final_10_maden,
        'final_11_maden': final_11_maden,
        'final_12_maden': final_12_maden,
    }
    return render(request, 'ostaz_details.html', context)


@login_required
def mezan(request):
    all_mezan = Mezan.objects.all()
    context = {
        'all_mezan': all_mezan,
    }
    return render(request, 'mezan.html', context)


@login_required
def add_tawseef(request):
    all_cats = Category.objects.all()
    add_category_form = AddCategoryForm(request.POST)
    if request.method == 'POST':
        if add_category_form.is_valid():
            form = add_category_form.save(commit=False)
            form.save()
            new_mezan = Mezan(name=form)
            new_mezan.save()
            return redirect('add_tawseef')
    else:
        add_category_form = AddCategoryForm()
    context = {
        'all_cats': all_cats,
        'add_category_form': add_category_form,
    }
    return render(request, 'add_tawseef.html', context)


@login_required
def delete_tawseef(request, pk):
    current_tawseef = get_object_or_404(Category, pk=pk)
    current_tawseef.delete()
    return redirect('add_tawseef')


class TawseefUpdate(UpdateView):
    model = Category
    fields = ['category_name', 'type']
    template_name_suffix = '_update_form'


@login_required
def add_new_daily(request, pk):
    current_type = get_object_or_404(Type, pk=pk)
    add_new_daily_form = AddNewDailyForm(request.POST, typz=current_type)
    if request.method == 'POST':
        if add_new_daily_form.is_valid():
            form = add_new_daily_form.save(commit=False)
            form.total_da2en = form.da2en
            form.total_maden = form.maden
            form.type = current_type
            form.save()
            current_farm = form.farm
            current_balance = Balance.objects.get(farm=current_farm)
            current_mezan = Mezan.objects.get(name=form.maden_from_cat)
            if form.maden != 0:
                added_balance = form.maden
                new_balance = int(current_balance.balance) - int(added_balance)
                current_balance.balance = new_balance
                current_balance.save()
                new_mezan_maden = int(current_mezan.maden) + int(added_balance)
                current_mezan.maden = new_mezan_maden
                current_mezan.save()
            if form.da2en != 0:
                added_balance = form.da2en
                new_balance = int(current_balance.balance) + int(added_balance)
                current_balance.balance = new_balance
                current_balance.save()
            return redirect('finance_daily')
    else:
        add_new_daily_form = AddNewDailyForm(typz=current_type)
    context = {
        'add_new_daily_form': add_new_daily_form,
        'current_type': current_type,
    }
    return render(request, 'add_new_daily.html', context)


def add_daily_one(request):
    add_daily_one_form = AddDailyOne(request.POST)
    if request.method == 'POST':
        if add_daily_one_form.is_valid():
            current_type = add_daily_one_form.cleaned_data['type']
            return redirect('/finance/adddaily/' + str(current_type.pk) + '/')
    else:
        add_daily_one_form = AddDailyOne()
    context = {
        'add_daily_one_form': add_daily_one_form,
    }
    return render(request, 'add_new_daily_one.html', context)


@login_required
def safes(request, pk):
    current_safe = get_object_or_404(Balance, pk=pk)
    current_farm = Farm.objects.get(farm_name=current_safe.farm.farm_name)
    balance = current_safe.balance
    farm_daily = Daily.objects.filter(farm=current_farm, is_invoice=False)
    all_invoice = Daily.objects.filter(farm=current_farm, is_invoice=True)
    all_buys = []
    all_sells = []
    for item in all_invoice:
        if item.maden != 0:
            all_buys.append(item.maden)
        if item.da2en != 0:
            all_sells.append(item.da2en)
    final_buys = sum(all_buys)
    final_sells = sum(all_sells)
    all_costs = []
    for item in farm_daily:
        if item.maden != 0:
            all_costs.append(item.maden)
    final_costs = sum(all_costs)
    costs = final_costs + final_buys
    net = final_sells - costs
    context = {
        'current_safe': current_safe,
        'balance': balance,
        'farm_daily': farm_daily,
        'final_costs': final_costs,
        'final_buys': final_buys,
        'final_sells': final_sells,
        'net': net,
    }
    return render(request, 'safes.html', context)


@login_required
def create_invoice_buy(request):
    add_buy_invoice_form = AddBuyInvoice(request.POST)
    if request.method == 'POST':
        if add_buy_invoice_form.is_valid():
            form = add_buy_invoice_form.save(commit=False)
            total = form.quantity * form.price
            form.total_price = total
            form.save()
            new_daily = Daily(text='فاتورة شراء رقم  ' + str(form.id), maden=form.total_price,
                              maden_from_type=form.category.type, maden_from_cat=form.category, da2en=0, farm=form.farm,
                              is_invoice=True, paid=form.total_price, unpaid=0)
            new_daily.save()
            current_balance = Balance.objects.get(farm=form.farm)
            new_balance = int(current_balance.balance) - int(form.total_price)
            current_balance.balance = new_balance
            current_balance.save()
            current_item = Warehouse.objects.filter(farm=form.farm, item_name=form.product)
            if current_item.count() != 0:
                current_item = Warehouse.objects.filter(farm=form.farm, item_name=form.product)[0]
                current_quantity = current_item.item_quantity
                added_quantity = form.quantity
                new_quantity = int(current_quantity) + int(added_quantity)
                current_item.item_quantity = new_quantity
                current_item.save()
                return redirect('report_buys')
            else:
                current_quantity = 0
                added_quantity = form.quantity
                new_quantity = int(current_quantity) + int(added_quantity)
                new_adding = Warehouse(item_name=form.product, item_quantity=new_quantity, farm=form.farm)
                new_adding.save()
                return redirect('report_buys')
    else:
        add_buy_invoice_form = AddBuyInvoice()
    context = {
        'add_buy_invoice_form': add_buy_invoice_form,
    }
    return render(request, 'create_buy_invoice.html', context)


@login_required
def create_invoice_sell(request):
    add_sell_invoice_form = AddSellInvoice(request.POST)
    if request.method == 'POST':
        if add_sell_invoice_form.is_valid():
            form = add_sell_invoice_form.save(commit=False)
            total = form.quantity * form.price
            form.total_price = total
            form.unpaid = int(total) - int(form.paid)
            form.save()
            new_daily = Daily(text='فاتورة بيع رقم  ' + str(form.id), da2en=form.total_price,
                              da2en_from_type=form.category.type, da2en_from_cat=form.category, maden=0, farm=form.farm,
                              is_invoice=True, unpaid=form.unpaid, paid=form.paid)
            new_daily.save()
            current_client_balance = form.client.client_balance
            added_client_balance = form.unpaid
            new_client_balance = int(current_client_balance) + int(added_client_balance)
            client_obj = form.client
            client_obj.client_balance = new_client_balance
            client_obj.save()
            current_balance = Balance.objects.get(farm=form.farm)
            new_balance = int(current_balance.balance) + int(form.paid)
            current_balance.balance = new_balance
            current_balance.save()
            current_item = Warehouse.objects.get(item_name=form.product, farm=form.farm)
            added_quant = int(current_item.item_quantity) - int(form.quantity)
            current_item.item_quantity = added_quant
            current_item.save()
            return redirect('invoice_details', form.pk)
    else:
        add_sell_invoice_form = AddSellInvoice()
    context = {
        'add_sell_invoice_form': add_sell_invoice_form,
    }
    return render(request, 'create_sell_invoice.html', context)


@login_required
def income_list(request):
    form1 = IncomeListFilterForm(request.GET, queryset=Daily.objects.filter(is_invoice=False))
    # all_daily = Daily.objects.filter(is_invoice=False)
    form2 = IncomeListFilterForm(request.GET, queryset=Daily.objects.filter(is_invoice=True))
    # all_invoice = Daily.objects.filter(is_invoice=True)
    all_sells = []
    all_buys = []
    for item in form2.qs:
        if item.da2en != 0:
            all_sells.append(item.da2en)
        if item.maden != 0:
            all_buys.append(item.maden)
    final_sells = sum(all_sells)
    final_buys = sum(all_buys)
    st_profit = final_sells - final_buys
    all_costs = []
    for item in form1.qs:
        if item.maden != 0:
            all_costs.append(item.maden)
    final_costs = sum(all_costs)
    net = st_profit - final_costs
    context = {
        'final_sells': final_sells,
        'final_buys': final_buys,
        'st_profit': st_profit,
        'final_costs': final_costs,
        'net': net,
        'filter1': form1,
        'filter2': form2,
    }

    return render(request, 'income_list.html', context)


@login_required
def report_all(request):
    all_balance = Balance.objects.all()
    total_bal = []
    for bal in all_balance:
        total_bal.append(bal.balance)
    final_total_bal = sum(total_bal)
    all_sales = SellInvoice.objects.all()
    total_sales = []
    for item in all_sales:
        total_sales.append(item.total_price)
    final_total_sells = sum(total_sales)
    all_buys = BuyInvoice.objects.all()
    total_buy = []
    for item in all_buys:
        total_buy.append(item.total_price)
    final_total_buys = sum(total_buy)
    taxes = 0
    one_net = final_total_sells - taxes
    all_costs = Daily.objects.filter(is_invoice=False)
    costs = []
    for item in all_costs:
        if item.maden != 0:
            costs.append(item.maden)
    final_costs = sum(costs)
    all_costs_and_buys = final_costs + final_total_buys
    final_net = final_total_sells - all_costs_and_buys
    context = {
        'all_balance': all_balance,
        'final_total_bal': final_total_bal,
        'all_sales': all_sales,
        'final_total_sells': final_total_sells,
        'taxes': taxes,
        'one_net': one_net,
        'final_total_buys': final_total_buys,
        'final_costs': final_costs,
        'final_net': final_net,
    }
    return render(request, 'reports/all.html', context)


@login_required
def report_farm(request):
    farm_report_form = FarmReportForm(request.POST)
    if request.method == 'POST':
        if farm_report_form.is_valid():
            farm_name = farm_report_form.cleaned_data['farm']
            return redirect('/farm/report/details/' + str(farm_name.pk))
    else:
        farm_report_form = FarmReportForm()
    context = {
        'farm_report_form': farm_report_form,
    }
    return render(request, 'reports/farm.html', context)


@login_required
def report_farm_details(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    current_balance = Balance.objects.get(farm=current_farm).balance
    all_sales = SellInvoice.objects.filter(farm=current_farm)
    total_sales = []
    for item in all_sales:
        total_sales.append(item.total_price)
    final_total_sells = sum(total_sales)
    taxes = 0
    one_net = final_total_sells - taxes
    all_buys = BuyInvoice.objects.filter(farm=current_farm)
    total_buy = []
    for item in all_buys:
        total_buy.append(item.total_price)
    final_total_buys = sum(total_buy)
    all_costs = Daily.objects.filter(is_invoice=False, farm=current_farm)
    costs = []
    for item in all_costs:
        if item.maden != 0:
            costs.append(item.maden)
    final_costs = sum(costs)
    all_costs_and_buys = final_costs + final_total_buys
    final_net = final_total_sells - all_costs_and_buys
    context = {
        'current_farm': current_farm,
        'current_balance': current_balance,
        'final_total_sells': final_total_sells,
        'taxes': taxes,
        'one_net': one_net,
        'final_total_buys': final_total_buys,
        'final_costs': final_costs,
        'final_net': final_net,
    }
    return render(request, 'reports/farm_details.html', context)


@login_required
def report_sales(request):
    form = SellInvoiceFilterForm(request.GET, queryset=SellInvoice.objects.filter().order_by('-date'))
    context = {
        'all_sells': form.qs,
        'filter': form,
    }
    return render(request, 'reports/sales.html', context)


@login_required
def report_buys(request):
    form = BuyInvoiceFilterForm(request.GET, queryset=BuyInvoice.objects.filter().order_by('-date'))
    context = {
        'all_sells': form.qs,
        'filter': form,
    }
    return render(request, 'reports/buys.html', context)


@login_required
def report_daily(request):
    form = DailyReportFilterForm(request.GET, queryset=Daily.objects.filter().order_by('-date'))
    context = {
        'all_daily': form.qs,
        'filter': form,
    }
    return render(request, 'reports/daily.html', context)


@login_required
def new_daily(request):
    new_daily_form = NewDailyForm(request.POST)
    if request.method == 'POST':
        if new_daily_form.is_valid():
            form = new_daily_form.save(commit=False)
            if form.da2en != 0:
                current_farm_balance = Balance.objects.get(farm=form.farm)
                added_balance = form.da2en
                new_balance = int(current_farm_balance.balance) + int(added_balance)
                current_farm_balance.balance = new_balance
                current_farm_balance.save()
                current_mezan = Mezan.objects.get(name=form.da2en_from_cat)
                old_mezan_da2en = current_mezan.da2en
                added_mezan_da2en = form.da2en
                new_mezan_da2en = int(old_mezan_da2en) + int(added_mezan_da2en)
                current_mezan.da2en = new_mezan_da2en
                current_mezan.save()
            if form.maden != 0:
                current_farm_balance = Balance.objects.get(farm=form.farm)
                added_balance = form.maden
                new_balance = int(current_farm_balance.balance) - int(added_balance)
                current_farm_balance.balance = new_balance
                current_farm_balance.save()
                current_mezan = Mezan.objects.get(name=form.maden_from_cat)
                old_mezan_maden = current_mezan.maden
                added_mezan_maden = form.maden
                new_mezan_maden = int(old_mezan_maden) + int(added_mezan_maden)
                current_mezan.maden = new_mezan_maden
                current_mezan.save()

            form.save()
            return redirect('finance_daily')
    else:
        new_daily_form = NewDailyForm()
    context = {
        'new_daily_form': new_daily_form,
    }
    return render(request, 'new_daily.html', context)


@login_required
def warehouse_details(request, pk):
    current_warehouse = get_object_or_404(Farm, pk=pk)
    all_items = Warehouse.objects.filter(farm=current_warehouse)
    context = {
        'current_warehouse': current_warehouse,
        'all_items': all_items,
    }
    return render(request, 'warehouse_details.html', context)


@login_required
def talab_sarf(request, pk):
    current_warehouse = get_object_or_404(Farm, pk=pk)
    create_talab_form = CreateTalabForm(request.POST)
    if request.method == 'POST':
        if create_talab_form.is_valid():
            form = create_talab_form.save(commit=False)
            form.farm = current_warehouse
            form.save()
            return redirect('/warehouse/' + str(pk))
    else:
        create_talab_form = CreateTalabForm()
    context = {
        'current_warehouse': current_warehouse,
        'create_talab_form': create_talab_form,
    }
    return render(request, 'talab_sarf.html', context)


@login_required
def talab_sarf_list(request):
    all_talab = Talabat.objects.all().order_by('-date')
    context = {
        'all_talab': all_talab,
    }
    return render(request, 'talabat_sarf_list.html', context)


@login_required
def talabat_delete(request, pk):
    current_talabat = get_object_or_404(Talabat, pk=pk)
    current_talabat.delete()
    return redirect('talab_sarf_list')


@login_required
def talabat_do(request, pk):
    current_talabat = get_object_or_404(Talabat, pk=pk)
    talabat_do_form = TalabatDoForm(request.POST)
    if request.method == 'POST':
        if talabat_do_form.is_valid():
            quantity = talabat_do_form.cleaned_data['quantity']
            product = talabat_do_form.cleaned_data['product']
            farm_from = talabat_do_form.cleaned_data['farm_from']
            print(farm_from)
            farm_to = current_talabat.farm
            farm_from_obj1 = Farm.objects.get(farm_name=str(farm_from))
            farm_from_obj = Warehouse.objects.get(farm=farm_from_obj1)
            current_quant = farm_from_obj.item_quantity
            removed_quant = quantity
            new_from_quant = int(current_quant) - int(removed_quant)
            farm_from_obj.item_quantity = new_from_quant
            farm_from_obj.save()
            farm_to_obj = Warehouse.objects.filter(farm=farm_to, item_name=product)
            if farm_to_obj.count() != 0:
                farm_to_obj = Warehouse.objects.filter(farm=farm_to, item_name=product)[0]
                current_to_quant = farm_to_obj.item_quantity
                added_to_quant = quantity
                new_to_quant = int(current_to_quant) + int(added_to_quant)
                farm_to_obj.item_quantity = new_to_quant
                farm_to_obj.save()
                current_talabat.OK = True
                current_talabat.save()
                return redirect('talab_sarf_list')
            else:
                new_to_added = Warehouse(item_name=product, item_quantity=quantity, farm=farm_to)
                new_to_added.save()
                current_talabat.OK = True
                current_talabat.save()
                return redirect('talab_sarf_list')

    else:
        talabat_do_form = TalabatDoForm()
    context = {
        'current_talabat': current_talabat,
        'talabat_do_form': talabat_do_form,
    }
    return render(request, 'talabat_do.html', context)


def load_cates(request):
    current_maden_type = request.GET.get('maden_from_type')
    cates = Category.objects.filter(type=current_maden_type)
    return render(request, 'aj/maden_from_cate_dropdown_list_options.html', {'cates': cates})


def load_cates_da2en(request):
    current_da2en_type = request.GET.get('da2en_from_type')
    cates_da2en = Category.objects.filter(type=current_da2en_type)
    return render(request, 'aj/da2en_from_cate_dropdown_list_options.html', {'cates_da2en': cates_da2en})


def mezania(request):
    osol_mota_obj = Type.objects.get(type_name='الاصول المتداولة ')
    all_daily_osol_mota_da2en = Daily.objects.filter(da2en_from_type=osol_mota_obj).values(
        'da2en_from_cat__category_name').annotate(
        all_da2en=Sum('da2en'))
    all_daily_osol_mota_maden = Daily.objects.filter(maden_from_type=osol_mota_obj).values(
        'maden_from_cat__category_name').annotate(
        all_maden=Sum('maden'))
    all_daily_osol_mota_total_maden = Daily.objects.filter(maden_from_type=osol_mota_obj).annotate(
        all_maden=Sum('maden'))
    all_daily_osol_mota_total_da2en = Daily.objects.filter(da2en_from_type=osol_mota_obj).annotate(
        all_da2en=Sum('da2en'))
    osol_mota_maden_list = []
    osol_mota_da2en_list = []
    for item in all_daily_osol_mota_total_maden:
        osol_mota_maden_list.append(item.all_maden)
    final_osol_mota_maden_total = sum(osol_mota_maden_list)
    for item in all_daily_osol_mota_total_da2en:
        osol_mota_da2en_list.append(item.all_da2en)
    final_osol_mota_da2en_total = sum(osol_mota_da2en_list)
    osol_mota_total_net = int(final_osol_mota_da2en_total) - int(final_osol_mota_maden_total)
    #############################################################
    osol_sabta_obj = Type.objects.get(type_name='الاصول الثابتة')
    all_daily_osol_sabta_da2en = Daily.objects.filter(da2en_from_type=osol_sabta_obj).values(
        'da2en_from_cat__category_name').annotate(
        all_da2en_osol_sabta=Sum('da2en'))
    all_daily_osol_sabta_maden = Daily.objects.filter(maden_from_type=osol_sabta_obj).values(
        'maden_from_cat__category_name').annotate(
        all_maden_osol_sabta=Sum('maden'))
    all_daily_osol_sabta_total_maden = Daily.objects.filter(maden_from_type=osol_sabta_obj).annotate(
        all_maden=Sum('maden'))
    all_daily_osol_sabta_total_da2en = Daily.objects.filter(da2en_from_type=osol_sabta_obj).annotate(
        all_da2en=Sum('da2en'))
    osol_sabta_maden_list = []
    osol_sabta_da2en_list = []
    for item in all_daily_osol_sabta_total_maden:
        osol_sabta_maden_list.append(item.all_maden)
    final_osol_sabta_maden_total = sum(osol_sabta_maden_list)
    for item in all_daily_osol_sabta_total_da2en:
        osol_sabta_da2en_list.append(item.all_da2en)
    final_osol_sabta_da2en_total = sum(osol_sabta_da2en_list)
    osol_sabta_total_net = int(final_osol_sabta_da2en_total) - int(final_osol_sabta_maden_total)
    # final total for osol
    net_osol = int(osol_mota_total_net) + int(osol_sabta_total_net)
    #############################################################################3
    #############################################################################3
    #############################################################################3
    khosom_mota_obj = Type.objects.get(type_name='الخصوم المتدوالة')
    all_daily_khosom_mota_da2en = Daily.objects.filter(da2en_from_type=khosom_mota_obj).values(
        'da2en_from_cat__category_name').annotate(
        all_da2en=Sum('da2en'))
    all_daily_khosom_mota_maden = Daily.objects.filter(maden_from_type=khosom_mota_obj).values(
        'maden_from_cat__category_name').annotate(
        all_maden=Sum('maden'))
    all_daily_khosom_mota_total_maden = Daily.objects.filter(maden_from_type=khosom_mota_obj).annotate(
        all_maden=Sum('maden'))
    all_daily_khosom_mota_total_da2en = Daily.objects.filter(da2en_from_type=khosom_mota_obj).annotate(
        all_da2en=Sum('da2en'))
    khosom_mota_maden_list = []
    khosom_mota_da2en_list = []
    for item in all_daily_khosom_mota_total_maden:
        khosom_mota_maden_list.append(item.all_maden)
    final_khosom_mota_maden_total = sum(khosom_mota_maden_list)
    for item in all_daily_khosom_mota_total_da2en:
        khosom_mota_da2en_list.append(item.all_da2en)
    final_khosom_mota_da2en_total = sum(khosom_mota_da2en_list)
    khosom_mota_total_net = int(final_khosom_mota_da2en_total) - int(final_khosom_mota_maden_total)
    #################################################################################################
    khosom_sabta_obj = Type.objects.get(type_name='الخصوم غير المتداولة')
    all_daily_khosom_sabta_da2en = Daily.objects.filter(da2en_from_type=khosom_sabta_obj).values(
        'da2en_from_cat__category_name').annotate(
        all_da2en=Sum('da2en'))
    all_daily_khosom_sabta_maden = Daily.objects.filter(maden_from_type=khosom_sabta_obj).values(
        'maden_from_cat__category_name').annotate(
        all_maden=Sum('maden'))
    all_daily_khosom_sabta_total_maden = Daily.objects.filter(maden_from_type=khosom_sabta_obj).annotate(
        all_maden=Sum('maden'))
    all_daily_khosom_sabta_total_da2en = Daily.objects.filter(da2en_from_type=khosom_sabta_obj).annotate(
        all_da2en=Sum('da2en'))
    khosom_sabta_maden_list = []
    khosom_sabta_da2en_list = []
    for item in all_daily_khosom_sabta_total_maden:
        khosom_sabta_maden_list.append(item.all_maden)
    final_khosom_sabta_maden_total = sum(khosom_sabta_maden_list)
    for item in all_daily_khosom_sabta_total_da2en:
        khosom_sabta_da2en_list.append(item.all_da2en)
    final_khosom_sabta_da2en_total = sum(khosom_sabta_da2en_list)
    khosom_sabta_total_net = int(final_khosom_sabta_da2en_total) - int(final_khosom_sabta_maden_total)
    net_khosom = int(khosom_sabta_total_net) + int(khosom_mota_total_net)
    ##################################################################################################
    ##################################################################################################
    ##################################################################################################
    rights_obj = Type.objects.get(type_name='حقوق الملكية')
    all_daily_rights_da2en = Daily.objects.filter(da2en_from_type=rights_obj).values(
        'da2en_from_cat__category_name').annotate(
        all_da2en=Sum('da2en'))
    all_daily_rights_maden = Daily.objects.filter(maden_from_type=rights_obj).values(
        'maden_from_cat__category_name').annotate(
        all_maden=Sum('maden'))
    all_daily_rights_total_maden = Daily.objects.filter(maden_from_type=rights_obj).annotate(all_maden=Sum('maden'))
    all_daily_rights_total_da2en = Daily.objects.filter(da2en_from_type=rights_obj).annotate(all_da2en=Sum('da2en'))
    rights_maden_list = []
    rights_da2en_list = []
    for item in all_daily_rights_total_maden:
        rights_maden_list.append(item.all_maden)
    final_rights_maden_total = sum(rights_maden_list)
    for item in all_daily_rights_total_da2en:
        rights_da2en_list.append(item.all_da2en)
    final_rights_da2en_total = sum(rights_da2en_list)
    rights_total_net = int(final_rights_da2en_total) - int(final_rights_maden_total)

    context = {
        # osoool
        'all_daily_osol_mota_maden': all_daily_osol_mota_maden,
        'all_daily_osol_mota_da2en': all_daily_osol_mota_da2en,
        'all_daily_osol_mota_total_maden': all_daily_osol_mota_total_maden,
        'all_daily_osol_mota_total_da2en': all_daily_osol_mota_total_da2en,
        'osol_mota_total_net': osol_mota_total_net,
        #############################################
        'all_daily_osol_sabta_maden': all_daily_osol_sabta_maden,
        'all_daily_osol_sabta_da2en': all_daily_osol_sabta_da2en,
        'all_daily_osol_sabta_total_maden': all_daily_osol_sabta_total_maden,
        'all_daily_osol_sabta_total_da2en': all_daily_osol_sabta_total_da2en,
        'osol_sabta_total_net': osol_sabta_total_net,
        # total osol
        'net_osol': net_osol,
        #################################################################
        # khosom
        'all_daily_khosom_mota_maden': all_daily_khosom_mota_maden,
        'all_daily_khosom_mota_da2en': all_daily_khosom_mota_da2en,
        'all_daily_khosom_mota_total_maden': all_daily_khosom_mota_total_maden,
        'all_daily_khosom_mota_total_da2en': all_daily_khosom_mota_total_da2en,
        'khosom_mota_total_net': khosom_mota_total_net,
        #########################################################################
        'all_daily_khosom_sabta_maden': all_daily_khosom_sabta_maden,
        'all_daily_khosom_sabta_da2en': all_daily_khosom_sabta_da2en,
        'all_daily_khosom_sabta_total_maden': all_daily_khosom_sabta_total_maden,
        'all_daily_khosom_sabta_total_da2en': all_daily_khosom_sabta_total_da2en,
        'khosom_sabta_total_net': khosom_sabta_total_net,
        # total_all_khosom
        'net_khosom': net_khosom,
        ###########################################################################
        # rights
        'all_daily_rights_maden': all_daily_rights_maden,
        'all_daily_rights_da2en': all_daily_rights_da2en,
        'all_daily_rights_total_maden': all_daily_rights_total_maden,
        'all_daily_rights_total_da2en': all_daily_rights_total_da2en,
        'rights_total_net': rights_total_net,

    }
    return render(request, 'mezania.html', context)


def safe_deposit(request, pk):
    safe_object = get_object_or_404(Balance, pk=pk)
    farm_object = safe_object.farm
    type_object = Type.objects.get(type_name='الاصول المتداولة ')
    cat_object = Category.objects.get(category_name='النقدية')
    safe_deposit_form = SafeDepositForm(request.POST)
    if request.method == 'POST':
        if safe_deposit_form.is_valid():
            amount = safe_deposit_form.cleaned_data['amount']
            safe_object.balance += amount
            safe_object.save()
            new_daily_object = Daily(text="إيداع فى الخزينة ", da2en=amount, farm=farm_object,
                                     da2en_from_type=type_object, da2en_from_cat=cat_object, paid=amount, unpaid=0)
            new_daily_object.save()
            return redirect('safes', pk=pk)
    else:
        safe_deposit_form = SafeDepositForm(request.POST)
    context = {
        'safe_object': safe_object,
        'safe_deposit_form': safe_deposit_form,
    }
    return render(request, 'safe_deposit.html', context)


def costs_add(request):
    company_obj1 = Company.objects.filter()
    company_obj = Company.objects.filter()[0]
    safe_obj1 = Balance.objects.filter()
    safe_obj = Balance.objects.filter()[0]
    farm_object = safe_obj.farm
    cat_object = Category.objects.get(category_name='النقدية')
    safe_costs_form = SafecostsForm(request.POST)
    if request.method == 'POST':
        if safe_costs_form.is_valid():
            amount = safe_costs_form.cleaned_data['amount']
            title = safe_costs_form.cleaned_data['title']
            type_object = Type.objects.get(type_name='الاصول المتداولة ')
            safe_obj.balance -= amount
            safe_obj.save()
            new_daily_object = Daily(text=title, maden=amount, farm=farm_object,
                                     maden_from_type=type_object, da2en_from_cat=cat_object, paid=amount, unpaid=0)
            new_daily_object.save()
            return redirect('safes', pk=safe_obj.pk)

    else:
        safe_costs_form = SafecostsForm(request.POST)
    context = {
        'safe_costs_form': safe_costs_form,
    }
    return render(request, 'costs_add.html', context)


def invoice_details(request, pk):
    current_invoice = get_object_or_404(SellInvoice, pk=pk)
    context = {
        'current_invoice': current_invoice,
    }
    return render(request, 'invoices_details.html', context)
