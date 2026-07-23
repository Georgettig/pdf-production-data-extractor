# 📄 PDF Production Data Extractor

Sistema desenvolvido em Python para automatizar a extração, tratamento e armazenamento de dados provenientes de relatórios de produção em formato PDF.

Esse projeto foi desenvolvido para solucionar um problema real observado durante minha atuação em uma indústria de papel e celulose.

Durante o processo produtivo, as máquinas geram automaticamente relatórios em formato PDF contendo indicadores operacionais. Esses indicadores são utilizados para análise de desempenho, acompanhamento da produção e tomada de decisão.

Antes da automação, a coleta e a digitação dessas informações eram realizadas de forma manual através de planilhas eletrônicas, tornando o processo repetitivo, demorado e suscetível a erros de digitação.

Portanto, o objetivo deste projeto foi automatizar toda essa etapa, transformando documentos PDF em dados estruturados prontos para consulta e análise posterior.

##  🏭 Contexto

Cada máquina de papel produz relatórios com informações relevantes, contendo informações relevantes sobre o processo.

Por conta disso, o sistema foi desenvolvido para:

- identificar automaticamente a máquina responsável pelo relatório;
- selecionar o parser adequado para aquele layout;
- extrair os dados específicos de cada modelo de documento;
- tratar e padronizar as informações;
- armazenar tudo em um banco de dados relacional.

# 🚀 Funcionalidades

✅ Upload de relatórios PDF
✅ Identificação automática da máquina de origem
✅ Extração automática dos indicadores de produção
✅ Tratamento e padronização dos dados
✅ Cadastro automático dos produtos
✅ Armazenamento em banco de dados SQLite
✅ Prevenção de registros duplicados
✅ Consulta de dados através de interface Streamlit

## 🏗 Arquitetura do projeto
```
pdf-production-data-extractor/
│
├── database/
│   ├── database.py          # 
│   ├── models.py            #
│   └── repository.py        #
│  
├── exemplos/
│   ├── 17072601.pdf         #
│   ├── 20072601.pdf         #
│   └── 220072601.pdf        #
│
├── machines/
│   ├── factory.py           #
│   └── machine.py           #
│
├── parsers/
│   ├── helpers.py           #
│   └── parser.py            #
│
├── app.py                   #
├── extractor.py             #
├── models.py                #
├── requirements.txt         #
└── README.md
```

## 🔄 Fluxo do processamento

```text
                 Upload do PDF
                       │
                       ▼
        Identificação do nome do arquivo
                       │
                       ▼
        Determinação da máquina de origem
                       │
                       ▼
         Extração dos dados do relatório
                       │
                       ▼
       Tratamento e padronização dos dados
                       │
                       ▼
      Verificação de registros duplicados
                       │
                       ▼
      Cadastro/Relacionamento do produto
                       │
                       ▼
         Armazenamento no banco SQLite
                       │
                       ▼
        Consulta através da interface
```

## ⚙️ Identificação automática da máquina

Durante a importação, o sistema identifica automaticamente a máquina de origem analisando o nome do arquivo, sem necessidade de intervenção do usuário.

Após essa identificação, o parser correspondente é selecionado automaticamente, garantindo que cada relatório seja processado utilizando as regras adequadas para o layout daquela máquina.

### Regras de identificação

| Máquina | Padrão do nome do arquivo | Exemplo |
|----------|---------------------------|----------|
| MP1 | Arquivos com **8 caracteres numéricos** | `17072601.pdf` |
| MP2 | Arquivos com **9 caracteres**, iniciando com **2** | `220072601.pdf` |

### Exemplo do funcionamento

| Arquivo recebido | Máquina identificada |
|------------------|----------------------|
| `17072601.pdf` | MP1 | 
| `17072615.pdf` | MP1 |
| `220072601.pdf` | MP2 | 
| `220072615.pdf` | MP2 | 

## 📊 Informações extraídas

O sistema realiza a extração automática de diversos indicadores presentes nos relatórios de produção, como:

- Número do rolo
- Produto
- Data de produção
- Produção total
- Tempo total de máquina
- Tempo de quebra
- Comprimento produzido
- Número de quebras
- Velocidade da enroladeira
- Largura do rolo
- Taxa de produção
- Gramatura (setpoint e média)
- Umidade (setpoint e média)
- Peso seco (setpoint e média)
- Temperatura (quando disponível)

Além de também identificar e armazenar parâmetros adicionais, como:

- Máquina responsável pela produção
- Arquivo de origem

## 🛡 Validações implementadas

Durante a importação dos relatórios, o sistema realiza diversas validações de maneira automática.

- Vefificação de registros duplicados.
- Tratamento de valores ausentes.
- Conversão de dados numéricos.
- Padronização de formatos.
- Relacionamento entre produtos e relatórios.
- Validação da integridade dos dados antes da gravação.

## 

## ⚙ Tecnologias utilizadas

### Linguagem:
- Python

### Interface:
- Streamlit

### Manipulação dos dados:
- Pandas

### Banco de dados:
- SQLite
- SQLAlchemy

### Leitura de PDFs:
- PyMuPDF

### Controle de versão:
- Git
- GitHub

## 📸 Demonstração

### Exemplo de PDF:

<img width="588" height="442" alt="image" src="https://github.com/user-attachments/assets/99c0a7cb-3e00-45f9-8c3d-28583340bbe9" />

### Tela inicial:

<img width="1242" height="204" alt="tela_inicial" src="https://github.com/user-attachments/assets/a64b3853-172f-4f11-bc28-1e5885a3f5b1" />

### Upload dos PDFs:

<img width="1200" height="590" alt="upload" src="https://github.com/user-attachments/assets/b24255e2-cf78-4510-91fe-b4861a264bb4" />

### Consulta dos dados:

<img width="631" height="225" alt="base_dados" src="https://github.com/user-attachments/assets/befc507d-00b2-4089-86eb-0acbda676f9e" />

## 💻 Como executar

Clone o repositório abaixo:

```bash
git clone https://github.com/Georgettig/pdf-production-data-extractor.git
```

Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente

```bash
.venv\Scripts\activate
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Execute a aplicação

```bash
streamlit run app.py
```

## 🎯 Objetivos do projeto

- Automatizar um processo realizado manualmente.
- Reduzir erros operacionais.
- Estruturar dados provenientes de documentos PDF.
- Disponibilizar informações para análises e indicadores.
- Demonstrar conhecimentos em Python e Engenharia de Dados aplicados a um cenário industrial real.

## 👨‍💻 Autor

**Guilherme Georgetti Albuquerque Galvão**

Engenheiro de Produção — UNESP

🔗 LinkedIn: *linkedin.com/in/guilherme-georgetti*
