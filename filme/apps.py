from django.apps import AppConfig
import os

class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import Usuario
        
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        # 1. Garante que as variáveis de ambiente existem
        if email and senha:
            # 2. Verifica a existência pelo USERNAME "admin" (e não apenas pelo e-mail)
            if not Usuario.objects.filter(username="admin").exists():
                Usuario.objects.create_superuser(
                    username="admin", 
                    email=email, 
                    password=senha
                )
            else:
                # 3. Caso já exista, apenas garante as permissões e ativação
                admin_user = Usuario.objects.get(username="admin")
                if not admin_user.is_staff or not admin_user.is_superuser:
                    admin_user.is_staff = True
                    admin_user.is_superuser = True
                    admin_user.is_active = True
                    admin_user.save()