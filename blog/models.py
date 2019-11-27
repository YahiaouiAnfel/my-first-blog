from django.conf import settings
from django.db import models
from django.utils import timezone

# c’est un endroit dans lequel nous définirons notre publication de blog.



class Post(models.Model):#c'est un object
    #models.Model signifie que la publication est un modèle Django, 
    #donc Django sait qu'il doit être enregistré dans la base de données.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#Ceci est un lien vers un autre modèle.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        #Pour créer un objet, instanciez-le à l'aide d'arguments mot-clé dans la classe de modèle, puis appelez-le save()pour l'enregistrer dans la base de données.
 
    def __str__(self):#"dunder" (abréviation de "double-underscore").
        return self.title

 #La dernière étape consiste à ajouter notre nouveau modèle à notre base de données. Nous devons d’abord faire savoir à Django que notre modèle a été modifié. (Nous venons de le créer!) Allez dans la fenêtre de votre console et tapez python manage.py makemigrations blog
 #Django a préparé pour nous un fichier de migration que nous devons maintenant appliquer à notre base de données. Le type python manage.py migrate bloget la sortie doivent être comme suit:
 