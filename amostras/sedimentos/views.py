from django.shortcuts import  render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import View
from .models import amostra
from .models import continente
from .models import cidade
from .models import estado
from .models import país
from .models import ambiente
from .models import clima
from .forms import UserForm, ContatoForm, amostraForm, continenteForm, paísForm, estadoForm, cidadeForm,climaForm,ambienteForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.db.models import Q


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def create_amostra(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = amostraForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            amostra = form.save(commit=False)
            amostra.user = request.user
            amostra.imagem = request.FILES['imagem']
            file_type = amostra.imagem.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'amostra': amostra,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'sedimentos/amostra_form.html', context)
            amostra.save()
            return render(request, 'sedimentos/detail.html', {'amostra': amostra})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/amostra_form.html', context)




def detail(request, amostra_id):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        user = request.user
        amostra = get_object_or_404(amostra, pk=amostra_id)
        return render(request, 'sedimentos/detail.html', {'amostra': amostra, 'user': user})


def delete_amostra(request, amostra_id):
    amostra = amostra.objects.get(pk=amostra_id)
    amostra.delete()
    amotras = amostra.objects.filter(user=request.user)
    return render(request, 'sedimentos/index.html', {'amostras': amotras})



def index(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        amostras = amostra.objects.filter(user=request.user)
        continente_results = continente.objects.all()
        query = request.GET.get("q")
        if query:
            amostras = amostras.filter(
                Q(codigo__icontains=query) |
                Q(tipo__icontains=query)
            ).distinct()
            continente_results = continente_results.filter(
                Q(nome__icontains=query)
            ).distinct()
            return render(request, 'sedimentos/index.html', {
                'amotras': amostras,
                'continentes': continente_results,
            })
        else:
            return render(request, 'sedimentos/index.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################
########################################################################################################################


def contid(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        continentes = continente.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            continentes = continentes.filter(
                Q(nome__icontains=query) |
                Q(sigla__icontains=query)
            ).distinct()
            return render(request, 'sedimentos/index.html', {
                'continentes': continentes,


            })
        else:
            return render(request, 'sedimentos/index.html', {'continentes': continentes})


def contd(request, continente_id):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        user = request.user
        continente = get_object_or_404(continente, pk=continente_id)
        return render(request, 'sedimentos/detail.html', {continente: continente, 'user': user})


def create_continente(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = continenteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            continente = form.save(commit=False)
            continente.user = request.user
            continente.save()
            return render(request, 'sedimentos/detail.html', {continente: continente})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/continente_form.html', context)


def delete_continente(request, continente_id):
    continente = continente.objects.get(pk=continente_id)
    continente.delete()
    continentes = continente.objects.filter(user=request.user)
    return render(request, 'sedimentos/contid.html', {'continentes': continentes})


########################################################################################################################
########################################################################################################################
########################################################################################################################


def index3(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        cidades = cidade.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            cidades = cidades.filter(
                Q(nome__icontains=query) |
                Q(estado__icontains=query)
            ).distinct()
            return render(request, 'sedimentos/index.html', {
                'cidades': cidades,

            })
        else:
            return render(request, 'sedimentos/index.html', {'cidades': cidades})


def detail5(request, cidade_id):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        user = request.user
        cidade = get_object_or_404(cidade, pk=cidade_id)
        return render(request, 'sedimentos/detail.html', {cidade: cidade, 'user': user})


def create_cidade(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = cidadeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            cidade = form.save(commit=False)
            cidade.user = request.user
            cidade.save()
            return render(request, 'sedimentos/detail.html', {cidade: cidade})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/cidade_form.html', context)


def delete_cidade(request, cidade_id):
    cidade = continente.objects.get(pk=cidade_id)
    cidade.delete()
    cidades = cidade.objects.filter(user=request.user)
    return render(request, 'sedimentos/detail.html', {'cidades': cidades})


########################################################################################################################
########################################################################################################################
########################################################################################################################

def index4(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        estados = estado.objects.filter(user=request.user)

        query = request.GET.get("q")
        if query:
            estados = estados.filter(
                Q(nome__icontains=query) |
                Q(país__icontains=query)
            ).distinct()
            return render(request, 'sedimentos/index.html', {
                'estados': estados,

            })
        else:
            return render(request, 'sedimentos/index.html', {'estados': estados})


def detail4(request, estado_id):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        user = request.user
        estado = get_object_or_404(estado, pk=estado_id)
        return render(request, 'sedimentos/detail.html', {estado: estado, 'user': user})


def create_estado(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = estadoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            estado = form.save(commit=False)
            estado.user = request.user
            estado.save()
            return render(request, 'sedimentos/detail.html', {estado: estado})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/estado_form.html', context)


def delete_estado(request, estado_id):
    estado = estado.objects.get(pk=estado_id)
    estado.delete()
    estados = estado.objects.filter(user=request.user)
    return render(request, 'sedimentos/index.html', {'estados': estados})

########################################################################################################################
########################################################################################################################
########################################################################################################################

def index5(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        paíss = país.objects.filter(user=request.user)

        query = request.GET.get("q")
        if query:
            paíss = paíss.filter(
                Q(nome__icontains=query) |
                Q(região__icontains=query)
            ).distinct()
            return render(request, 'sedimentos/index.html', {
                'paíss': paíss,

            })
        else:
            return render(request, 'sedimentos/index.html', {' paíss ': paíss})


def detail3(request, país_id):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        user = request.user
        país = get_object_or_404(país, pk=país_id)
        return render(request, 'sedimentos/detail.html', {país: país, 'user': user})


def create_país(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = paísForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            país = form.save(commit=False)
            país.user = request.user
            país.save()
            return render(request, 'sedimentos/detail.html', {país: país})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/país_form.html', context)


def delete_país(request, país_id):
    país = país.objects.get(pk=país_id)
    país.delete()
    paíss = país.objects.filter(user=request.user)
    return render(request, 'sedimentos/index.html', {' paíss': paíss})

########################################################################################################################
########################################################################################################################
########################################################################################################################

def index6(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        ambientes = ambiente.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            ambientes = ambientes.filter(
                Q(tipo__icontains=query) |
                Q(amostra__icontains=query)
            ).distinct()
            return render(request, 'sedimentos/index.html', {
                'ambientes': ambientes,

            })
        else:
            return render(request, 'sedimentos/index.html', {'ambientes': ambientes})


def detail6(request, ambiente_id):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        user = request.user
        ambiente = get_object_or_404(ambiente, pk=ambiente_id)
        return render(request, 'sedimentos/detail.html', {ambiente: ambiente, 'user': user})


def create_ambiente(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = ambienteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            ambiente = form.save(commit=False)
            ambiente.user = request.user
            ambiente.save()
            return render(request, 'sedimentos/detail.html', {ambiente: ambiente})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/ambiente_form.html', context)


def delete_ambiente(request, ambiente_id):
    ambiente = ambiente.objects.get(pk=ambiente_id)
    ambiente.delete()
    ambientes = ambiente.objects.filter(user=request.user)
    return render(request, 'sedimentos/index.html', {'ambientes': ambientes})

########################################################################################################################
########################################################################################################################
########################################################################################################################
def index7(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        climas =clima.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            climas = climas.filter(
                Q(tipo__icontains=query)

            ).distinct()
            return render(request, 'sedimentos/index.html', {
                'climas': climas,

            })
        else:
            return render(request, 'sedimentos/index.html', {'climas': climas})


def detail7(request, clima_id):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        user = request.user
        clima = get_object_or_404(clima, pk=clima_id)
        return render(request, 'sedimentos/detail.html', {clima: clima, 'user': user})


def create_clima(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = climaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            clima = form.save(commit=False)
            clima.user = request.user
            clima.save()
            return render(request, 'sedimentos/detail.html', {clima: clima})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/clima_form.html', context)


def delete_clima(request, clima_id):
    clima = clima.objects.get(pk=clima_id)
    clima.delete()
    climas = clima.objects.filter(user=request.user)
    return render(request, 'sedimentos/index.html', {'climas': climas})

########################################################################################################################
########################################################################################################################
########################################################################################################################
class UserFormView(View):
    form_class=UserForm
    template_name='sedimentos/register_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                return redirect('sedimentos:index')
        return render(request, self.template_name, {'form': form})

########################################################################################################################
########################################################################################################################
########################################################################################################################
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'sedimentos/login.html', context)

########################################################################################################################
########################################################################################################################
########################################################################################################################
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                amostras = amostra.objects.filter(user=request.user)
                return render(request, 'sedimentos/index.html', {'amostras': amostras})
            else:
                return render(request, 'sedimentos/login.html', {'error_message': 'Sua conta foi desativada'})
        else:
                return render(request, 'sedimentos/login.html', {'error_message': ' Login Invalido '})
    return render(request, 'sedimentos/login.html')

########################################################################################################################
########################################################################################################################
########################################################################################################################

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                amostras = amostra.objects.filter(user=request.user)
                return render(request, 'sedimentos/index.html', {'amostras': amostras})
    context = {
        "form": form,
    }
    return render(request, 'sedimentos/register_form.html', context)

########################################################################################################################
########################################################################################################################
########################################################################################################################
def contato(request):
    form_class = ContatoForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            Nome = request.POST.get('Nome', '')
            Email = request.POST.get('Email', '')
            Mensagem = request.POST.get('Mensagem', '')
            template = get_template('sedimentos/contato.html')
            context = Context({
                'Nome': Nome,
                'Email': Email,
                'Mensagem': Mensagem,
            })

            content = template.render(context)

            email =EmailMessage (
                "New contact form submission", content, "Adiministração" + '', ['fabio.carvalho.souza@usp.br'],
                headers={'Reply-To': Email}
            )
            email.send()
            return redirect('contato')
    return render(request, 'sedimentos/contato.html', {'form': form_class, })

########################################################################################################################
########################################################################################################################
########################################################################################################################
def adicionar(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'sedimentos/adicionar.html', context)



########################################################################################################################
########################################################################################################################
########################################################################################################################
def continentes(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            continente_ids = []
            for amostra in amostra.objects.filter(user=request.user):
                for continente in amostra.continente_set.all():
                    continente_ids.append(continente.pk)
            users_continentes = continente.objects.filter(pk__in=continente_ids)
            if filter_by == 'favorites':
                users_continentes = users_continentes.filter(is_favorite=True)
        except amostra.DoesNotExist:
            users_continentes = []
        return render(request, 'sedimentos/continentes.html', {
            'continente_list': users_continentes,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################
########################################################################################################################
def paíss(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            país_ids = []
            for amostra in amostra.objects.filter(user=request.user):
                for país in amostra.país_set.all():
                    país_ids.append(país.pk)
            users_paíss = país.objects.filter(pk__in=país_ids)
            if filter_by == 'favorites':
                users_paíss = users_paíss.filter(is_favorite=True)
        except amostra.DoesNotExist:
            users_paíss = []
        return render(request, 'sedimentos/paíss.html', {
            'país_list': users_paíss,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################
########################################################################################################################
def estados(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            estado_ids = []
            for amostra in amostra.objects.filter(user=request.user):
                for estado in amostra.estado_set.all():
                    estado_ids.append(estado.pk)
            users_estados = estado.objects.filter(pk__in=estado_ids)
            if filter_by == 'favorites':
                users_estados = users_estados.filter(is_favorite=True)
        except amostra.DoesNotExist:
            users_estados = []
        return render(request, 'sedimentos/estados.html', {
            'estado_list': users_estados,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################
########################################################################################################################

def cidades(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            cidade_ids = []
            for amostra in amostra.objects.filter(user=request.user):
                for cidade in amostra.cidade_set.all():
                    cidade_ids.append(cidade.pk)
            users_cidades = cidade.objects.filter(pk__in=cidade_ids)
            if filter_by == 'favorites':
                users_cidades = users_cidades.filter(is_favorite=True)
        except amostra.DoesNotExist:
            users_cidades = []
        return render(request, 'sedimentos/cidades.html', {
            'cidade_list': users_cidades,
            'filter_by': filter_by,
        })


########################################################################################################################
########################################################################################################################
########################################################################################################################
def climas(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            clima_ids = []
            for amostra in amostra.objects.filter(user=request.user):
                for clima in amostra.clima_set.all():
                    clima_ids.append(clima.pk)
            users_climas = clima.objects.filter(pk__in=clima_ids)
            if filter_by == 'favorites':
                users_climas = users_climas.filter(is_favorite=True)
        except amostra.DoesNotExist:
            users_climas = []
        return render(request, 'sedimentos/climas.html', {
            'clima_list': users_climas,
            'filter_by': filter_by,
        })
########################################################################################################################
########################################################################################################################
########################################################################################################################
def ambientes(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            ambiente_ids = []
            for amostra in amostra.objects.filter(user=request.user):
                for ambiente in amostra.ambiente.all():
                    ambiente_ids.append(ambiente.pk)
            users_ambientes = ambiente.objects.filter(pk__in=ambiente_ids)
            if filter_by == 'favorites':
                users_ambientes = users_ambientes.filter(is_favorite=True)
        except amostra.DoesNotExist:
            users_ambientes = []
        return render(request, 'sedimentos/ambientes.html', {
            'ambiente_list': users_ambientes,
            'filter_by': filter_by,
        })
########################################################################################################################
########################################################################################################################
########################################################################################################################