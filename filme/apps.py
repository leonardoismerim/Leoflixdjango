from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'


    def ready(self):
        from .models import Usuario
        import os
    
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        usuarios = Usuario.objects.filter(email=email)
        if not Usuario.objects.filter(username='admin').exists():
            Usuario.objects.create_superuser(username='admin', email='email', password='senha')
            
        else:
            # Caso o usuário admin já exista no banco sem permissão de staff
            user = Usuario.objects.get(username='admin')
            user.is_staff = True
            user.is_superuser = True
            user.save()