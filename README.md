# Django_Carros
## Repositório do Projeto de estudos sobre Carros.
### 07 - Django e Banco de Dados (models e admin)
- 037 Configurando o Admin do nosso model Car.
    - Primeiro criamos a classe do nosso modelo em models.py que seriam os campos da nossa tabela.
    - Segundo registramos na admin.py do nosso app cars a CarAdmin e registramos para o sistema enxergar.

### Comandos.
- python -m venv venv - Cria a máquina virtual.
- venv/Scripts/activate - Abre a máquina virtual para uso da aplicação.
- pip install django - Com a máquina virtual aberta, instalando django.
- django-admin startproject app . - Inicializando a aplicação, será app, mas pode ser qualquer nome.
- django-admin --version - Para olhar qual a versão do Django.
- python manage.py runserver - Para inicar a aplicação no servidor web ou navegador.
- python manage.py startapp cars - Inicia nosso app ou modolo app, foi atribuido o nome cars, mas poderia ser qualquer outro.
- python manage.py makemigrations - para criar a atualizar nossas tabelas.
- python manage.py migrate - executa o comando de criação das tabelas.
- python manege.py createsuperuser - Criar o super usuário do sistema, user root.