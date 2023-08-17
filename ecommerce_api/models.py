


from django.db import models


    

class Properties(models.Model):
    id_pro = models.AutoField(primary_key=True)  
    nom_pro   = models.CharField(max_length=255)
    type_pro = models.CharField(max_length=255)
    
    
    
class Category(models.Model):
    id_cat = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='category_icons/')
    created_at = models.DateTimeField(auto_now_add=True)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)
    prop =  models.ForeignKey(Properties, on_delete=models.CASCADE)
    
    
class Article(models.Model):
    id_art = models.AutoField(primary_key=True)
    code_art = models.CharField(max_length=100)
    titre = models.CharField(max_length=255)    
    photos = models.ImageField(upload_to='pics/', blank=True, null=True)  # ImageField for photos
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categorie_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_deleted = models.BooleanField(default=False)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    is_booster = models.BooleanField(default=False)
    forme_colis = models.CharField(max_length=100)
    
 


class Favori(models.Model):
    id_fav = models.AutoField(primary_key=True)
    article = models.ForeignKey( Article , on_delete=models.CASCADE)




