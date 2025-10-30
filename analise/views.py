from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from .forms import ComentarioForm
from .analise_sentimento import AnaliseSentimento
from .models import ComentarioModel
from textblob import TextBlob
from deep_translator import GoogleTranslator
from django.core.paginator import Paginator
# Para o sistema de lofin e cadastro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

@login_required
def analisar_comentario_form(request):
    resultado = None

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario_model = form.save(commit=False)  # pega o objeto mas não salva ainda
            comentario = comentario_model.texto         # o texto digitado

            # Traduz do português para inglês
            comentario_en = GoogleTranslator(source='pt', target='en').translate(comentario)

            # Analisa com TextBlob em inglês
            blob = TextBlob(comentario_en)
            polaridade = blob.sentiment.polarity

            if polaridade > 0:
                resultado = "Positivo"
            elif polaridade < 0:
                resultado = "Negativo"
            else:
                resultado = "Neutro"

            # Salva no banco o comentário original + resultado
            ComentarioModel.objects.create(
                texto=comentario,
                sentimento=resultado
            )
    else:
        form = ComentarioForm()

    return render(request, "analise/analisar.html", {"form": form, "resultado": resultado})

@login_required
def historico(request):
    comentarios_list = ComentarioModel.objects.all().order_by('-data')
    
    paginator = Paginator(comentarios_list, 5)  # 5 comentários por página
    page_number = request.GET.get('page')
    comentarios = paginator.get_page(page_number)

    return render(request, "analise/historico.html", {"comentarios": comentarios})

@login_required
def grafico_sentimentos(request):
    comentarios = ComentarioModel.objects.all()
    
    positivos = comentarios.filter(sentimento="Positivo").count()
    negativos = comentarios.filter(sentimento="Negativo").count()
    neutros = comentarios.filter(sentimento="Neutro").count()

    # Criar gráfico
    fig, ax = plt.subplots()
    ax.bar(['Positivo', 'Negativo', 'Neutro'], [positivos, negativos, neutros], color=['green','red','gray'])
    ax.set_title("Distribuição de Sentimentos")
    
    # Converter gráfico para base64 para exibir no HTML
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagem_png = buffer.getvalue()
    grafico_base64 = base64.b64encode(imagem_png).decode('utf-8')
    buffer.close()

    return render(request, "analise/grafico.html", {"grafico": grafico_base64})

@login_required
def editar_comentario(request, id):
    comentario = get_object_or_404(ComentarioModel, id=id)   # 👈 usa ComentarioModel
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('historico')
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'analise/editar.html', {'form': form, 'comentario': comentario})

@login_required
def deletar_comentario(request, id):
    comentario = get_object_or_404(ComentarioModel, id=id)
    if request.method == "POST":
        comentario.delete()
        return redirect('historico')
    return render(request, 'analise/confirmar_exclusao.html', {'comentario': comentario})

# Cadastro
def cadastrar(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # loga automaticamente após cadastro
            return redirect("historico")
    else:
        form = UserCreationForm()
    return render(request, "analise/cadastrar.html", {"form": form})

# Entrar no sistema
def entrar(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("historico")
    else:
        form = AuthenticationForm()
    return render(request, "analise/login.html", {"form": form})

# Sair do sistema
def sair(request):
    logout(request)
    return redirect("entrar")
