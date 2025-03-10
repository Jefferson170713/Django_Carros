# Django_Carros
## Repositório do Projeto de estudos sobre Carros.
### 07 - Django e Banco de Dados (models e admin)
- __037 - Configurando o Admin do nosso model Car__.
    - Primeiro criamos a classe do nosso modelo em __models.py__ que seriam os campos da nossa tabela.
    - Segundo registramos na __admin.py__ do nosso app cars a __CarAdmin__ e registramos para o sistema enxergar.
- __038 - Configurações adicionais do nosso projeto__.
    - Ajustando o __models.py__ na class para trazer o nome dos objetos que foram adicionados.
    - Subscrevendo a função `def __str__(self)`:
- __039 - Criando modelo e admin de marcas (ForeignKey)__. 
    - Criando a nova classe Brand para ser a chave estrangeira em Car.
    - Colocando o __models.ForeignKey( Brand, on_delete=models.PROTECT, related_name='car_brand' )__.
    - Brand: Para adicionar a classe como chave estrangeira.
    - on_delete: Com PROTECT serve para evitar a exclusão em cascata se a marca for removida e ainda tiver dados no banco.
- __040 - Armazenando imagens dos carros__.
    - Adição da coluna placa e foto no nosso modelo. Onde foto é __ImageField e uoload_to__ na pasta cars e que ficará dentro de `media/`.
    - Depois adicionamos o `'brand__name'` para a pesquisar em search_fields de pesquisa em __admin.py__ para não dar erro.
    - Configuramos `MEDDIA_ROOT` e `MEDIA_URL`, as pastas padrão para armazenamento de arquivos do nosso modelo. Lembrando de importar a biblioteca __os__.
    - Em `urls.py` colocamos `from django.conf import settings`, `from django.conf.urls.static import static` para as pastas onde iremos armazenar os arquivos funcionar corretamente.
    - Por fim, adicionar no __urlpatterns__ as duas pastas.
### Comandos.
- __python -m venv venv__ - Cria a máquina virtual.
- __venv/Scripts/activate__ - Abre a máquina virtual para uso da aplicação.
- __pip install django__ - Com a máquina virtual aberta, instalando django.
- __django-admin startproject app .__ - Inicializando a aplicação, será app, mas pode ser qualquer nome.
- __django-admin --version__ - Para olhar qual a versão do Django.
- __python manage.py runserver__ - Para inicar a aplicação no servidor web ou navegador.
- __python manage.py startapp cars__ - Inicia nosso app ou modolo app, foi atribuido o nome cars, mas poderia ser qualquer outro.
- __python manage.py makemigrations__ - para criar a atualizar nossas tabelas.
- __python manage.py migrate__ - executa o comando de criação das tabelas.
- __python manege.py createsuperuser__ - Criar o super usuário do sistema, user root.