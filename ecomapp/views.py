from django.shortcuts import render,redirect
from ecomapp.models import Category,Product,Signup,Cart
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required(login_url='login1')
def admin_home(request):
    return render(request,'admin_home.html')

@login_required(login_url='login1')
def user_home(request):
    catagory=Category.objects.all()
    return render(request,'user_home.html',{'catagory':catagory})

def signup1(request):
    return render(request,'signup.html')

def login1(request):
    return render(request,'login.html')

@login_required(login_url='login1')
def add_catagorypage(request):
    return render(request,'add_catagory.html')
     

@login_required(login_url='login1')
def add_catagory(request):
    if request.method == 'POST':
        catagory_name = request.POST.get('catagory')
        category = Category(category_name=catagory_name)
        category.save()
        messages.error(request, 'New Category Added')
        return redirect('add_catagorypage')
    else:
        return render(request, 'add_catagory.html')


@login_required(login_url='login1')
def add_productpage(request):
    catagory=Category.objects.all()
    return render(request,'add_product.html', {'catagory':catagory})

@login_required(login_url='login1')
def add_product(request):
    if request.method=='POST':
        product_name=request.POST['product_name']
        description=request.POST['description']
        price=request.POST['price']
        image=request.FILES.get('file')
        sel=request.POST['sel']
        catagory=Category.objects.get(id=sel)
        product=Product(product_name=product_name,description=description, price=price, image=image,category=catagory)
        print('Save data')
        messages.error(request, 'New Product added')
        product.save()
        return redirect('add_productpage')

@login_required(login_url='login1')
def view_product(request):
    product=Product.objects.all()
    return render(request,'view_product.html',{'product':product})

@login_required(login_url='login1')
def delete(request,pk):
    p=Product.objects.get(id=pk)
    p.delete()
    messages.error(request, 'Product Deleted')
    return redirect('view_product')


def signup(request):
    if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address = request.POST['address']
        contact_number = request.POST['number']
        image = request.FILES.get('file') 
        if password != confirm_password:
            # Handle password mismatch error
            messages.error(request, "Password doesn't match")
            return render(request, 'signup.html')
        auth_user = User.objects.create_user( username=username, email=email, password=password)
        
        auth_user.save()
        user = Signup(user=auth_user, address=address, contact_number=contact_number, image=image)
        user.save()
        return redirect('login1')
    
def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                messages.info(request, f'Welcome {username}')
                return redirect('admin_home')
            else:
                auth.login(request, user)
                messages.info(request, f'Welcome {username}')
                return redirect('user_home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login1')
    return render(request, 'home.html')

@login_required(login_url='login1')
def view_user(request):
    user=Signup.objects.all()
    return render(request,'view_user.html',{'user':user})

@login_required(login_url='login1')
def delete_user(request,tid):
    users=Signup.objects.get(user_id=tid)
    users=users.user
    users.delete()
    messages.error(request, 'Deleted User')
    return redirect('view_user')
    

@login_required(login_url='login1')            
def logout(request):
     auth.logout(request)
     return redirect('home')

@login_required(login_url='login1') 
def products_page(request):
    products=Product.objects.all()
    return render(request,'productpage.html',{'products':products})

@login_required(login_url='login1')
def products_by_catagory(request):
    category_id=request.GET.get('catagory')
    category=Category.objects.get(id=category_id)
    products=Product.objects.filter(category=category)
    return render(request,'productpage.html',{'products':products, 'category':category})

@login_required(login_url='login1')
def cart_details(request, id):
    product = Product.objects.get(id=id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart')
    else:
        return redirect('cart') 
   

@login_required(login_url='login1')    
def cart(request):
    cart_items=Cart.objects.filter(user=request.user).select_related('product')
    total_price=sum(item.total_price() for item in cart_items)
    return render(request,'cart.html',{'cartitems':cart_items, 'totalprice':total_price})  


@login_required(login_url='login1')
def decrease_quantity(request, id):
    cart_item = Cart.objects.get(user=request.user, product_id=id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')
@login_required(login_url='login1')
def increase_quantity(request, id):
    cart_item = Cart.objects.get(user=request.user, product_id=id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required(login_url='login1')
def remove_cart(request,id):
    product=Product.objects.get(id=id)
    cart_item=Cart.objects.filter(user=request.user, product=product).first()
    
    if cart_item:
        cart_item.delete()
        return redirect('cart')

def navbar2(request):
    cart_items_count=Cart.objects.filter(user=request.user).count()
    category=Category.objects.all()
    return render(request,'user_home.html',{'category':category, 'cart_items_count':cart_items_count})
    
    