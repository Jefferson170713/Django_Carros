# Django_Carros
## Repositório do Projeto de estudos sobre Carros.
### 07 - Django e Banco de Dados (models e admin)
- 037 Configurando o Admin do nosso model Car.
    - Primeiro criamos a classe do nosso modelo em models.py que seriam os campos da nossa tabela.
    - Segundo registramos na admin.py do nosso app cars a CarAdmin e registramos para o sistema enxergar.
- 038 - Configurações adicionais do nosso projeto.
    - Ajustando o models.py na class para trazer o nome dos objetos que foram adicionados.
    - Subscrevendo a função def __str__(self):
- 039 - Criando modelo e admin de marcas (ForeignKey). 
    - Criando a nova classe Brand para ser a chave estrangeira em Car.
    - Colocando o models.ForeignKey( Brand, on_delete=models.PROTECT, related_name='car_brand' ).
    - Brand: Para adicionar a classe como chave estrangeira.
    - on_delete: Com PROTECT serve para evitar a exclusão em cascata se a marca for removida e ainda tiver dados no banco.
- 040 - Armazenando imagens dos carros.
    - Adição da coluna placa e foto no nosso modelo. Onde foto é ImageField e uoload_to na pasta cars e que ficará dentro de media/.
    - Depois adicionamos o 'brand__name' para a pesquisar em search_fields de pesquisa em admin.py para não dar erro.
    - Configuramos MEDDIA_ROOT e MEDIA_URL, as pastas padrão para armazenamento de arquivos do nosso modelo. Lembrando de importar a biblioteca __os__.
    - Em urls.py colocamos from django.conf import settings, from django.conf.urls.static import static para as pastas onde iremos armazenar os arquivos funcionar corretamente.
    - Por fim, adicionar no urlpatterns as duas pastas.
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