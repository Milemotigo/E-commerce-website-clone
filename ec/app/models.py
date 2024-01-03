from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATE_CHOICES = (
    ('Abia Umuahia', 'Abia Umuahia'),
    ('Adamawa Yola', 'Adamawa Yola'),
    ('Akwa Ibom Uyo', 'Akwa Ibom Uyo'),
    ('Anambra Awka', 'Anambra Awka'),
    ('Bauchi Bauchi', 'Bauchi Bauchi'),
    ('Bayelsa Yenagoa', 'Bayelsa Yenagoa'),
    ('Benue Makurdi', 'Benue Makurdi'),
    ('Borno Maiduguri', 'Borno Maiduguri'),
    ('Cross River Calabar', 'Cross River Calabar'),
    ('Delta Asaba', 'Delta Asaba'),
    ('Ebonyi Abakaliki', 'Ebonyi Abakaliki'),
    ('Edo Benin City', 'Edo Benin City'),
    ('Ekiti Ado-Ekiti', 'Ekiti Ado-Ekiti'),
    ('Enugu Enugu', 'Enugu Enugu'),
    ('Gombe Gombe', 'Gombe Gombe'),
    ('Imo Owerri', 'Imo Owerri'),
    ('Jigawa Dutse', 'Jigawa Dutse'),
    ('Kaduna Kaduna', 'Kaduna Kaduna'),
    ('Kano Kano', 'Kano Kano'),
    ('Katsina Katsina', 'Katsina Katsina'),
    ('Kebbi Birnin Kebbi', 'Kebbi Birnin Kebbi'),
    ('Kogi Lokoja', 'Kogi Lokoja'),
    ('Kwara Ilorin', 'Kwara Ilorin'),
    ('Lagos Ikeja', 'Lagos Ikeja'),
    ('Nasarawa Lafia', 'Nasarawa Lafia'),
    ('Niger Minna', 'Niger Minna'),
    ('Ogun Abeokuta', 'Ogun Abeokuta'),
    ('Ondo Akure', 'Ondo Akure'),
    ('Osun Osogbo', 'Osun Osogbo'),
    ('Oyo Ibadan', 'Oyo Ibadan'),
    ('Plateau Jos', 'Plateau Jos'),
    ('Rivers Port Harcourt', 'Rivers Port Harcourt'),
    ('Sokoto Sokoto', 'Sokoto Sokoto'),
    ('Taraba Jalingo', 'Taraba Jalingo'),
    ('Yobe Damaturu', 'Yobe Damaturu'),
    ('Zamfara Gusau', 'Zamfara Gusau'),
    ('Federal Capital Territory Abuja', 'Federal Capital Territory Abuja')
)

CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    @property
    def total_cost(self):
        return self.product.discounted_price * self.qualtity
    
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('packed', 'packed'),
    ('On.The.Way', 'On.The.Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('pending', 'pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=False)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=False)
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=False)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE, default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
