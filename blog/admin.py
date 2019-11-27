from django.contrib import admin
from .models import Post

admin.site.register(Post)
#Comme vous pouvez le constater, nous importons (incluons) le modèle Post défini dans le chapitre précédent.
# Pour que notre modèle soit visible sur la page d'administration, 
# nous devons enregistrer le modèle avec admin.site.register(Post).
#Pour vous connecter, vous devez créer un superutilisateur - un compte d'utilisateur qui contrôle tout sur le site