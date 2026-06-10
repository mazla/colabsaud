import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User

# --- CONFIGURE SEU ACESSO AQUI ---
USUARIO = 'admin'
EMAIL = 'colabsaud@gmail.com'
SENHA = 'colabadmin'  # <--- Escolha a sua senha aqui dentro das aspas
# ----------------------------------

if not User.objects.filter(username=USUARIO).exists():
    User.objects.create_superuser(USUARIO, EMAIL, SENHA)
    print("Sucesso: Conta de administrador criada automaticamente!")
else:
    print("Aviso: O administrador já existe no sistema.")