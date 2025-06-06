# Django_Carros
## Repositório do Projeto de estudos sobre Carros.
---
### 07 - Django e Banco de Dados (models e admin)

- __037 - Configurando o Admin do nosso model Car__.
    - Primeiro criamos a classe do nosso modelo em __models.py__ que seriam os campos da nossa tabela.
    - Segundo registramos na __admin.py__ do nosso app cars a __CarAdmin__ e registramos para o sistema enxergar.

- __038 - Configurações adicionais do nosso projeto__.
    - Ajustando o __models.py__ na class para trazer o nome dos objetos que foram adicionados.
    - Subscrevendo a função `def __str__(self)`:

- __039 - Criando modelo e admin de marcas (ForeignKey)__. 
    - Criando a nova classe Brand para ser a chave estrangeira em Car.
    - Colocando o `models.ForeignKey( Brand, on_delete=models.PROTECT, related_name='car_brand' )`.
    - Brand: Para adicionar a classe como chave estrangeira.
    - on_delete: Com PROTECT serve para evitar a exclusão em cascata se a marca for removida e ainda tiver dados no banco.

- __040 - Armazenando imagens dos carros__.
    - Adição da coluna placa e foto no nosso modelo. Onde foto é __ImageField e uoload_to__ na pasta cars e que ficará dentro de `media/`.
    - Depois adicionamos o `'brand__name'` para a pesquisar em search_fields de pesquisa em __admin.py__ para não dar erro.
    - Configuramos `MEDDIA_ROOT` e `MEDIA_URL`, as pastas padrão para armazenamento de arquivos do nosso modelo. Lembrando de importar a biblioteca __os__.
    - Em `urls.py` colocamos `from django.conf import settings`, `from django.conf.urls.static import static` para as pastas onde iremos armazenar os arquivos funcionar corretamente.
    - Por fim, adicionar no __urlpatterns__ as duas pastas.

- __045 - Retornando Templates para o usuário__ - Vamos aprender a usar arquivos css e js.
    - Primeiro no __settings.py__ temos que adicionar `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`.
    - Por conveção, sempre que criarmos uma pasta para uso é padrão colocar o nome da nossa aplicação `cars`.
    - Após isso, criaremos __2 pastas statics__
        - 1°: Dentro da aplicação normal.
        - 2°: Uma dentro de Cars, com ela criar as pastas de arquivos css e js para usar na aplicação.
    - Criar uma pasta __templates__ dentro de `cars`
    ```plaintext
    Django_Carros/
                ├── cars/
                │   ├── static/
                │   │   ├── cars/
                │   │   │   ├── css/
                │   │   │   │   └── css.css
                │   ├── templates/
                │   │   ├── cars/
                │   │   │   └── cars_index.html
                │   ├── models.py
                │   ├── views.py
                │   ├── ...
                ├── static/
                ├── manage.py
                ├── ...
    ```
- __046 - Linguagem de Templates do Django__ - Amostra de como passar os parâmetros simples do banco para a página que desejamos passar.
    - Criamos também no arquivo de `views.py` do nosso projeto o usso da Biblioteca `import locale`.
    - Função para retornar valores inteiros (int).
        - ```plaintext
            def format_int(value):
                return locale.format_string('%.f', value, grouping=True)
            ```
        
    - Função para retornar valores do tipo ponto flutuante(float).
        - ```plaintext
            def format_float(value):
                return locale.format_string('%.2f', value, grouping=True)
            ```

- __047 - Buscando carros no Banco de Dados com Django ORM__ - Mostrando como passar os dados que ADM insere no banco e como isso seria mostrado aos clientes.
    - Criamos uma página simples de HTML assim como um CSS somente para visualizar os dados.
    - Mas o ponto importante é como isso é passado do banco para o site, atraves da `views.py`.
    - Usamos `cars = Car.objects.all()` para passar todos as instâncias que estão no banco.

- __050 - Filtrando carros com os parâmetros do usuário__ - Filtrando com um campo de busca na página inicial para buscar os carros que queremos.
    - Primeeiro alteramos a `views.py` para passar o contexto e com isso passar todos os parâmetros necessários, com a variável __context__.
        - ```plaintext
            context = {'cars': cars, 'search': search,}
            ```

    - Com a variável __context__ sendo passada para a página, podemos agora acessar diretamente. Exemplo abaixo do uso direto.
        - ```plaintext
            <input type="search" name="search" class="search_input" placeholder="Pesquisar" value="{{ search }}">
        ```
        - ```
                {% if cars %}
                    {% for car in cars %}
                        <div class="item">
                            <h2 class="titulo"><strong>{{ car.model }}</strong></h2>
                            <p class="text">ID : <strong>{{ car.id }}</strong></p>
                            <p class="preco">R$ {{ car.value }}</p>
                            <p class="text">Marca : <strong>{{ car.brand }}</strong></p>
                            <p class="text">Ano de fabricação: <strong>{{ car.factory_year }}</strong></p>
                            <p class="text">Ano do modelo: <strong>{{ car.model_year }}</strong></p>
                            <p class="text-plate">Placa: <strong>{{ car.plate }}</strong></p>
                        </div>
                    {% endfor %}
                {% else %}
                    <div class="item">
                        <p class="text">Nenhum carro encontrado para a pesquisa "<strong>{{ search }}</strong>".</p>
                    </div>
                {% endif %}

            ```
- __053 - Configurando o base template__ - Contruindo um modelo padrão para o nosso projeto e de acordo com o contexto, mudamos as estruturas.

    - Em __settings.py -> TEMPLATES__, precisamos incluir a pasta templetes, crie se ela não exixtir.

    - Podemos também criar templetes dentro do nosso app que construímos, e dentro dele colocar o nosso __namespacy__.

    - Podemos e estamos usando os recuros de `include` na `cars_index.html` para exibir em nossa views.
        - ```plaintext
            {% extends 'cars/base_template.html' %}
            ```

    - Dessa forma, funciona nas minhas views e posso fazer alterações de forma mais simples sem usar por enquanto o recurso de `partials`.
        - ```plaintext
            {% include 'cars/header_search.html' %}
            ```

    - Fiz mais 2 arquivos para implementar nossa aplicação, `header_search.html` e `footer_base.html` para funcionar na página.

### 10 - Forms no Django

- __055 - Criando nosso primeiro Form__ - Criando meu primeiro form para adicionar novos veículos.

    - 1° - Criamos a view `new_car` que irá retornar a página `cars/new_car.html`.

        - 1.1 - Inicializamos dentro da view `new_car_form = CarForm()` para passar para o contexto da página, inicialmente vazia.

    - 2° - É preciso criar o arquivo `forms.py` dentro do nosso app de __cars__. 

        - 2.1 - Importar a biblioteca `from django import forms`. 

        - 2.2 - Importar a biblioteca `from cars.models import Brand` para usar na classe, pois ela é chave estrangeira.

        - 2.3 - Com a criação da classe, precisamos atribuir `queryset=Brand.objects.all()`, para a seleção de nossas marcas cadastradas no sistema.

        ```plaintext
            class CarForm(forms.Form):
                model = forms.CharField(max_length=150)
                brand = forms.ModelChoiceField(queryset=Brand.objects.all())
                factory_year = forms.IntegerField()
                model_year = forms.IntegerField()
                plate = forms.CharField(max_length=10)
                value = forms.FloatField()
                photo = forms.ImageField()
        ```

    - 3° - No template de `new_car.html`.

        - 3.1 - Dentro do formulário da página usamos __multipart/form-data__ assim `<form action="" method="POST" enctype="multipart/form-data">` para passar para dentro do banco vários parâmetros ao mesmo tempo.

        - 3.2 - Para critérios de segurança do __Django__ usamos `{% csrf_token %}` em todos os formulários.

        - 3.3 - E dentro do __context__, passamos.
        
        ```plaintext
            {% block content %}
                <form action="" method="POST" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ new_car_form.model }}
                    {{ new_car_form.brand }}
                    {{ new_car_form.factory_year }}
                    {{ new_car_form.model_year }}
                    {{ new_car_form.value }}
                    {{ new_car_form.plate }}
                    {{ new_car_form.photo }}
                    <input type="submit" value="Cadastrar" />
                </form>
            {% endblock %}
        ```

- __056 - Finalizando o cadastro de um novo carro__ - Para que eu possa salvar meus dados novos. 

    - 1° - Trabalhamos primeiro na `views.py --> new_car`.

        - 1.2 - Importamos `from cars.forms import Carform` para usar na `views.py` na `new_car`. Precisamos também importar a função __redirect__ `from django.shortcuts import redirect` para redirecionar as nossas urls.

        - 1.2 - Precisamos validar qual método está vindo se é __POST__ ou __GET__.

        - 1.3 - Depois precisamos pegar o que vem de __request.POST__ e __request.FILES__, nesse caso request.FILES porque temos um arquivo de imagem. Ficando assim `new_car_form = CarForm(request.POST, request.FILES)`.

        - 1.4 - Testamos se a condicação e os campos preenchidos estão válidos `if new_car_form.is_valid():`.

        - 1.5 - Precisamos então criar uma função para salvar que não vem nativo do __forms.py__ --> `new_car_form.save()`.

        - Mostrando como ficou ...

        ```plaintext
            from django.shortcuts import render, redirect
            ...
            from cars.forms import CarForm

            ...

            def new_car( request ):
                if request.method == 'POST':
                    new_car_form = CarForm(request.POST, request.FILES)
                    if new_car_form.is_valid():
                        new_car_form.save()
                        return redirect('cars:cars_index')
                else:
                    new_car_form = CarForm()

                context ={
                    'new_car_form': new_car_form,
                }
                return render(
                    request, 
                    'cars/new_car.html',
                    context,
                )
        ```

    - 2° - No arquivo de `forms.py` vamos importar __Car__ e criar a função save().

        - 2.1 - Importando Car `from cars.models import Car`.

        - 2.2 - Criando a função __save__.

            - 2.2.1 - Instanciamos car e atribuímos de acordo com o que está em __models.py__.

            - 2.2.2 - Ficando assim:

            ```plaintext
                def save(self):
                    car = Car(
                        model = self.cleaned_data['model'],
                        brand = self.cleaned_data['brand'],
                        factory_year = self.cleaned_data['factory_year'],
                        model_year = self.cleaned_data['model_year'],
                        plate = self.cleaned_data['plate'],
                        value = self.cleaned_data['value'],
                        photo = self.cleaned_data['photo']
                    )
                    car.save()
                    return car
            ```

- __057 - Migrando para ModelForm__ - Salvando de forma mais simples com ModelForms.

    - 1° - Precisa instanciar `from cars.models import Car`.

    - 2° - Com a classe *Meta* que define os metadados em modelos de formulários no Django, é usada para associar ao formulário do a um modelo.

        - 2.1 - Em `modelo = Car` associa o formulário ao modelo Car.

        - 2.2 - Em `fields = '__all__'` é um *Dunder method* que serve para atribuir todos os campos dos formulários que estamos tentando inserir, inclusive futuras modificações. 

    - 3° - Como ficou:

        ```plaintext
            class CarModelForm(forms.ModelForm):
                class Meta:
                    model = Car
                    fields = '__all__'
        
        ```
    
    - 4° - Após isso precisamos ir em `views.py` e alterar a *new_car*.

        - 1 - Na views *new_car* onde tinha `Carfom` substitui por `CarModelForm`.

        - Ficando assim:

            ```plaintext
                def new_car( request ):
                    if request.method == 'POST':
                        new_car_form = CarModelForm(request.POST, request.FILES)
                        if new_car_form.is_valid():
                            new_car_form.save()
                            return redirect('cars:cars_index')
                    else:
                        new_car_form = CarModelForm()

                    context ={
                        'new_car_form': new_car_form,
                    }
                    return render(
                        request, 
                        'cars/new_car.html',
                        context,
                    )
            ```

- __058 - Criando validações__ - No *ModelForms* criaremos validações personalizadas.

    - 1° - Para criar __*validações*__ no *ModelForm*, existe um padrão que o próprio Django identifica.

        - 1.1 - Por exemplo na aplicação que estou construindo, no meu modelo tem um campo que se chama *model*, e o padrão de validação do *ModelForm* da função é `clean_` antes do nome de qualquer modelo. Ficando assim `clean_<nome_do_campo>()`.

        - 1.2 - de como ficou `def clean_moodel(self):` após isso vem a sua regra de negócio que vai de acordo com a sua aplicaçao.

    - 2° - Outro passa importante é que fica inserido dentro do classe de *ModelForm*.

    - 3° - Ficando assim:

        ```plaintext
            def clean_value(self):
                value = self.cleaned_data.get('value')
                if value < 20000:
                    self.add_error('value', 'O valor não pode ser menor que R$ 20.000,00!')
                return value
        ```

- __059 - Introdução ao módulo__ - O que é o *auth_user* no Django? 
    
    - 1° - O *auth_user* é o modelo padrão do Django para representar usuários no sistema. Ele faz parte do app *django.contrib.auth.forms* e é usado para autenticação, autorização e gerenciamento de usuários.
    
    - 2° - Sistema de Autenticação do Django (`auth_user`), fica `*django.contrib.auth.forms*`.
    
    - 3° - Principais Campos do Modelo `auth_user`: 

        - 3.1 - **`username`** : Nome de usuário único.
        - 3.2 - **`password`**: Senha do usuário (armazenada de forma segura com hashing).
        - 3.3 - **`email`**: Endereço de e-mail do usuário.
        - 3.4 - **`first_name`**: Primeiro nome do usuário.
        - 3.5 - **`last_name`**: Sobrenome do usuário.
        - 3.6 - **`is_staff`**: Indica se o usuário pode acessar o Django Admin.
        - 3.7 - **`is_superuser`**: Indica se o usuário tem todas as permissões (superusuário).
        - 3.8 - **`is_active`**: Indica se o usuário está ativo.
        - 3.9 - **`last_login`**: Data e hora do último login.
        - 3.10 - **`date_joined`**: Data e hora em que o usuário foi criado.

- __060 - Criando nossa rota de registro de usuários__ - Primeiro vamos criar um app separado, no terminal digitaremos *python manage.py startapp accounts* somente para os usuários *o nome accounts é genérico mas poderia ser outro*, como acesso e teste de senhas.
    - 1° - No coração do nosso sistema ou em *app*, no arquivo de __*settings.py*__.

        - 1.1 Vamos em *INSTALLED_APPS* e registrar nosso novo app.
    
    - 2° - Vamos primeiro criar uma nova rota para integrar ao nosso sistema,
        - 2.1 - Vamos em *urls.py* do nosso app e 
        - 2.2 - importamos a views `from accounts.views import register_view`
        - 2.3 - Adicionamos a na url `path('', register_view, name='register'),`.
        - 2.4 - Agora vamos criar o arquivo de *urls.py* em *accounts*.
            ```plaintext
                from django.urls import path
                from accounts.views import register_view

                app_name = 'accounts'

                urlpatterns = [
                    path('register/', register_view, name='register'),
                ]
            ```
    - 3° - Criando a *views.py de accounts*.
        - 3.1 - É um formulário embutido do Django que facilita a criação de novos usuários. Ele já inclui campos como *username, password1 e password2 (para confirmação de senha)*.
        - 3.2 para criar ...
            ```plaintext
                from django.shortcuts import render
                from django.contrib.auth import UserCreationForm

                def register_view(request):
                    user_form = UserCreationForm()
                    return render(request, 'accounts/register.html', {'user_form': user_form})            
            ```
    - 4° - Agora vamos criar a pasta *templates* e o *register.html* de __*accounts*__.
        - 4.1 - usamos o atributo *{% csrf_token %}* para dar segurança e ficando assim: 
        ````plaintext
            {% block content %}
                <div class="fomulario">
                    <h1>Registrar</h1>
                    <form action="" method="POST">
                        {% csrf_token %}
                        <div>
                            <label for="id_username" >Usuário:</label>
                            {{ user_form.username }}
                        </div>
                        <div>
                            <label for="id_password1">Senha:</label>
                            {{ user_form.password1 }}
                        </div>
                        <div>
                            <label for="id_password2">Confirmação de Senha:</label>
                            {{ user_form.password2 }}
                        </div>
                        <button type="submit">Cadastrar</button>
                    </form>
                </div>
            {% endblock %}
        ````
- __061 - Registrando nosso primeiro usuário__ - Agora vamos registrar nosso primeiro usuário no sistema.
    - 1° - Vamos em *views.py* e adicionar o método de *POST* para registrar o usuário.
        ```plaintext
            from django.contrib.auth import UserCreationForm
            from django.shortcuts import render, redirect

            def register_view(request):
                if request.method == 'POST':
                    user_form = UserCreationForm(request.POST)
                    if user_form.is_valid():
                        user_form.save()
                        return redirect('accounts:login')
                else:
                    user_form = UserCreationForm()
                return render(request, 'accounts/register.html', {'user_form': user_form})
        ```
    - 2° - Para  fazer o registro de segurança se o usuário já existe, usamos o método `is_valid()` que já vem embutido no Django.
    - 3° - Após isso, redirecionamos para a página de login, que ainda não existe, mas já deixamos o caminho certo.
    - 4° - Agora para verificar se o usuário já existe com o mesmo nome cadastrado em nossa base de dados. Acrescetamos o seguinte código no *register.html* no erro de  `{{ user_form.username.errors }}` e em `{{ user_form.password1.errors }}` e  `{{ user_form.password2.errors }}`. Com isso, se o usuário já existir, ele vai mostrar o erro de que o usuário já existe. veja o eexemplo abaixo:

        ```plaintext
            <div>
                {{ user_form.username.errors }}
                <label for="id_username" >Usuário:</label>
                {{ user_form.username }}
            </div>         
        ```
- __062 - Criando a tela de login__ - Agora vamos criar a nossa tela de login, onde o usuário irá acessar o sistema.
    - 1° - Vamos primeiramente em *views.py*  de *accounts* e criar a view de login.
        - 1.1 - Importamos `from django.contrib.auth.forms import AuthenticationForm` para usar o formulário de autenticação do Django.
            - Com isso, podemos criar o formulário de login. Pois o Django já tem um formulário de autenticação pronto para uso.
        - 1.2 - Importamos também `from django.contrib.auth import login, logout` para fazer o login e logout do usuário.
        - 1.3 - Criamos a view de login, que irá renderizar o formulário de autenticação e processar o login do usuário.
            ```plaintext
                from django.shortcuts import render, redirect
                from django.contrib.auth.forms import AuthenticationForm
                from django.contrib.auth import login, logout

                ...

                def login_view(request):
                    if request.method == 'POST':
                        username = request.POST['username']
                        password = request.POST['password']
                        
                        user = authenticate(request, username=username, password=password)

                        if user is not None:
                            login(request, user)
                            return redirect('cars:cars_index')
                    else:
                        login_form = AuthenticationForm()
                    return render( request, 'accounts/login.html', {'login_form': login_form})

                ...

                def logout_view(request):
                    logout(request)
                    return redirect('accounts:login')

                ...

            ```
            - 1.4 - No código acima, verificamos se o método é *POST*, se for, pegamos o nome de usuário e a senha do formulário de autenticação.
            - 1.5 - Usamos a função `authenticate()` para verificar se o usuário existe e se a senha está correta.
            - 1.6 - Se o usuário for autenticado com sucesso, usamos a função `login()` para fazer o login do usuário e redirecionamos para a página de carros.
            - 1.7 Com a função `logout_view()`, podemos fazer o logout do usuário e redirecioná-lo para a página de login.

    - 2° - Agora vamos criar a rota de login e logout em *urls.py* de *accounts*.
        - 2.1 - Importamos a view de login `from accounts.views import login_view`.
        - 2.2 - Adicionamos a rota de login `path('login/', login_view, name='login'),`.
        - 2.3 - Ficando assim:
            ```plaintext
                from django.urls import path
                from accounts.views import register_view, login_view

                app_name = 'accounts'

                urlpatterns = [
                    path('register/', register_view, name='register'),
                    path('login/', login_view, name='login'),
                    path('logout/', logout_view, name='logout'),
                ]
            ```
    - 3° - Agora vamos criar o template de login em *accounts/templates/accounts/login.html*.
        - 3.1 - Vamos usar o formulário de autenticação do Django, que já vem pronto para uso.
        - 3.2 - Vamos usar o atributo *{% csrf_token %}* para dar segurança e ficando assim:
        ```plaintext
            {% block content %}
                <div class="fomulario">
                    <h1>Login</h1>
                    <form action="" method="POST">
                        {% csrf_token %}
                        <div>
                            <label for="id_username">Usuário:</label>
                            {{ login_form.username }}
                        </div>
                        <div>
                            <label for="id_password">Senha:</label>
                            {{ login_form.password }}
                        </div>
                        <button type="submit">Entrar</button>
                    </form>
                </div>
            {% endblock %}
        ```
---

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