from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    #  category_id
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static/img/', blank=True)
    bookAuthor = models.CharField(max_length=100)
    yearOfPublication = models.PositiveIntegerField(blank=True)
    Publisher = models.CharField(max_length=100, blank=True)
    ImageURLS = models.CharField(max_length= 250,blank=False)
    ImageURLM = models.CharField(max_length=250)
    ImageURLS = models.CharField(max_length=250)
    ISBN = models.CharField(max_length=20)


    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])



        


class bookRating(models.Model):
   product_id = models.ForeignKey(Product, on_delete=models.CASCADE) 
   UserID = models.ForeignKey(
       User,
        on_delete=models.CASCADE
    )
   bookRating = models.PositiveIntegerField()

    # def __init__(self, arg):
    #     super(bookRating, self).__init__()
    #     self.arg = arg
                        