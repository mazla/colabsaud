import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User

USUARIO = 'admin'
EMAIL = 'contato@colabsaud.com'
SENHA = 'ColabAdmin696'

user, created = User.objects.get_or_create(username=USUARIO, defaults={'email': EMAIL})

if created:
    user.set_password(SENHA)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print("Sucesso: Conta de administrador criada automaticamente!")
else:
    user.set_password(SENHA)
    user.save()
    print("Sucesso: Senha do administrador atualizada com sucesso!")