# Coment IA 🤖💬
### *Análise Inteligente de Sentimentos em Comentários*

---

## 📋 Sobre o Projeto

O **Coment IA** é um sistema inovador desenvolvido em Django que utiliza processamento de linguagem natural através da biblioteca **TextBlob** para analisar automaticamente o sentimento por trás de cada comentário inserido. Ideal para empresas, redes sociais e qualquer plataforma que queira entender melhor o feedback dos usuários.

---

## ✨ Funcionalidades Principais

### 🧠 **Análise de Sentimentos Automática**
- Classificação instantânea de comentários em:
  - ✅ **Positivo** - Comentários favoráveis e elogiosos
  - ❌ **Negativo** - Críticas e feedbacks negativos
  - ⚪ **Neutro** - Informações neutras ou sem carga emocional

### 📊 **Histórico Inteligente**
- **Tabela organizada** com todos os comentários analisados
- **Sistema de paginação** para navegação eficiente
- Visualização completa do texto, data/hora e classificação

### 📈 **Dashboard Visual**
- **Gráfico interativo** gerados com **Matplotlib**
- Visualização da distribuição de sentimentos
- Métricas e insights sobre os padrões de comentários

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python Django
- **IA & NLP:** TextBlob para análise de sentimentos
- **Visualização de Dados:** Matplotlib
- **Frontend:** HTML, CSS, Bootstrap
- **Banco de Dados:** SQLite

---

## 🚀 Como Usar

### 1. Adicionar Comentário
- Acesse a página principal
- Digite seu comentário no campo designado
- Clique em "Analisar"
- Receba instantaneamente a classificação do sentimento

### 2. Consultar Histórico
- Navegue até a aba "Histórico"
- Veja todos os comentários em tabela paginada
- Use a paginação para navegar entre os resultados

### 3. Visualizar Gráficos
- Acesse a página "Dashboard"
- Analise os gráficos de distribuição de sentimentos
- Entenda visualmente os padrões dos comentários

---

## 🎯 Exemplos de Análise

| Comentário | Classificação |
|------------|---------------|
| "Adorei o produto, muito bom!" | ✅ Positivo |
| "Não gostei, péssima qualidade" | ❌ Negativo |
| "Chegou na data combinada" | ⚪ Neutro |

---

## 🔧 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/coment-ia.git

# Entre no diretório
cd coment-ia

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
