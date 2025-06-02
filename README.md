# 📝 Gerador de Planilhas de Campo para Inventários Florestais

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://higuchip-gerador-planilha-main-qm20bv.streamlit.app/)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF%20Generation-orange.svg)
![GitHub stars](https://img.shields.io/github/stars/higuchip/gerador_planilha)
![GitHub last commit](https://img.shields.io/github/last-commit/higuchip/gerador_planilha)
![GitHub repo size](https://img.shields.io/github/repo-size/higuchip/gerador_planilha)


**Aplicação web para geração automatizada de planilhas de campo padronizadas para inventários florestais**

Desenvolvido por [Pedro Higuchi](https://www.linkedin.com/in/pedro-higuchi-4085a81b/)

---

## 📖 Descrição

O **Gerador de Planilhas de Campo** é uma aplicação web desenvolvida em Streamlit que automatiza a criação de planilhas padronizadas para inventários florestais. A ferramenta elimina contratempos comuns como urgências de última hora e perda de arquivos, oferecendo uma solução rápida e prática para profissionais da área florestal.

### 🎯 Funcionalidades Principais

- **📝 Geração Automática**: Criação instantânea de planilhas em PDF
- **🔒 Segurança Robusta**: Validação completa de entradas e proteção contra ataques
- **📊 Flexibilidade**: Suporte para até 2.000 árvores por planilha
- **🎨 Layout Profissional**: Planilhas formatadas e prontas para campo
- **💾 Download Direto**: Arquivo PDF gerado na hora para impressão
- **🚀 Interface Simples**: Processo em 3 passos intuitivos

---

## 🚀 Demo Online

Acesse a versão online da aplicação: **[Gerador de Planilhas de Campo](https://higuchip-gerador-planilha-main-qm20bv.streamlit.app/)**

---

## 🛠️ Tecnologias Utilizadas

### Principais Bibliotecas

| Biblioteca | Versão | Função |
|------------|--------|---------|
| `streamlit` | Latest | Interface web interativa |
| `reportlab` | Latest | Geração de documentos PDF |
| `pathlib` | Built-in | Manipulação segura de caminhos |
| `uuid` | Built-in | Geração de identificadores únicos |
| `html` | Built-in | Sanitização de entradas |

### Características Técnicas

- **🐍 Python 3.8+**: Compatibilidade moderna
- **📄 PDF Generation**: ReportLab para criação profissional
- **🔐 Security First**: Validação e sanitização completas
- **💨 Performance**: Arquivos temporários com limpeza automática

---

## 📋 Pré-requisitos

### Python 3.8+
```bash
python --version  # Deve ser 3.8 ou superior
```

### Bibliotecas Necessárias
- Streamlit (interface web)
- ReportLab (geração de PDF)

---

## 🔧 Instalação

### 1. Clone o Repositório
```bash
git clone https://github.com/higuchip/gerador-planilhas-campo.git
cd gerador-planilhas-campo
```

### 2. Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a Aplicação
```bash
streamlit run main.py
```

---

## 🎮 Como Usar

### **Passo 1: Responsável Técnico** 👤
- Informe o nome do profissional responsável pelo inventário
- Aceita letras, números, espaços e acentos
- Limite: 100 caracteres

### **Passo 2: Identificação da Área** 🌲
- Digite o nome ou código da área de estudo
- Formato flexível para diferentes nomenclaturas
- Limite: 100 caracteres

### **Passo 3: Configuração da Planilha** 📊
- Defina o número de árvores a serem medidas
- Intervalo: 1 a 2.000 árvores
- Valor padrão: 50 árvores

### **Resultado: Download Automático** 📥
- PDF gerado instantaneamente
- Layout profissional com campos organizados
- Pronto para impressão e uso em campo

---

## 📊 Estrutura da Planilha Gerada

### **Cabeçalho:**
- Título: "PLANILHA DE CAMPO - INVENTÁRIO FLORESTAL"
- Área de estudo identificada
- Campo para data do levantamento
- Responsável técnico especificado
- Espaço para equipe de campo

### **Tabela de Dados:**
| Campo | Descrição | Largura |
|-------|-----------|---------|
| **Parc.** | Número da parcela | 0.5" |
| **Núm.** | Número sequencial da árvore | 0.5" |
| **Espécie** | Nome da espécie identificada | 2.0" |
| **CAP/DAP** | Circunferência ou diâmetro | 1.5" |
| **Alt.** | Altura da árvore | 0.5" |
| **Obs** | Observações gerais | 1.5" |

### **Características:**
- ✅ **Grade completa** para facilitar preenchimento
- ✅ **Repetição de cabeçalho** em páginas múltiplas
- ✅ **Numeração automática** de páginas
- ✅ **Layout otimizado** para papel A4

---

## 🔒 Recursos de Segurança

### Validações Implementadas
- ✅ **Sanitização de entrada**: Remoção de caracteres perigosos
- ✅ **Limitação de tamanho**: Prevenção de overflow
- ✅ **Validação de tipos**: Verificação de dados numéricos
- ✅ **Path traversal protection**: Segurança de arquivos
- ✅ **Arquivos temporários**: Limpeza automática
- ✅ **Logging seguro**: Rastreamento de operações

### Limites de Segurança
- **Texto máximo**: 100 caracteres por campo
- **Árvores máximas**: 2.000 por planilha
- **Caracteres permitidos**: Letras, números, espaços, acentos, hífen, underscore, ponto
- **Arquivos temporários**: Removidos automaticamente após download


---

## 🌟 Casos de Uso

### **Inventários Florestais Comerciais**
- Levantamentos para manejo florestal
- Estudos de viabilidade econômica
- Monitoramento de crescimento

### **Pesquisa Acadêmica**
- Dissertações e teses
- Projetos de iniciação científica
- Estudos ecológicos

### **Consultoria Ambiental**
- Relatórios de impacto ambiental
- Planos de manejo de UCs
- Laudos técnicos

### **Órgãos Governamentais**
- Fiscalização ambiental
- Monitoramento de áreas protegidas
- Inventários de patrimônio público

---

## 🚀 Roadmap de Desenvolvimento

### **Versão Atual (1.0)**
- ✅ Geração básica de planilhas
- ✅ Interface web funcional
- ✅ Validações de segurança
- ✅ Download em PDF

### **Próximas Versões**

---

## 🤝 Contribuindo

### Como Contribuir
1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. **Commit** suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um **Pull Request**

### Diretrizes de Contribuição
- Siga o padrão **PEP 8** para Python
- Adicione **testes** para novas funcionalidades
- Mantenha a **documentação** atualizada
- Preserve a **compatibilidade** com Python 3.8+
- Foque na **segurança** e **usabilidade**

### Áreas para Contribuição
- 🐛 **Correção de bugs**
- ✨ **Novas funcionalidades**
- 📚 **Melhoria da documentação**
- 🔒 **Aprimoramentos de segurança**
- 🎨 **Interface do usuário**
- 🧪 **Testes automatizados**

---

## 🐛 Solução de Problemas

### Problemas Comuns

#### 1. Erro de Instalação do ReportLab
```bash
# Windows
pip install --upgrade setuptools wheel
pip install reportlab

# Linux/Mac
sudo apt-get install python3-dev  # Ubuntu/Debian
pip install reportlab
```

#### 2. Streamlit não Inicia
```bash
# Verifique a versão do Python
python --version

# Reinstale o Streamlit
pip uninstall streamlit
pip install streamlit
```

#### 3. PDF não é Gerado
- Verifique se o ReportLab está instalado corretamente
- Confirme se há espaço em disco disponível
- Teste com dados simples (poucos caracteres)

#### 4. Caracteres Especiais não Aparecem
- O sistema suporta acentos padrão em português
- Caracteres muito especiais são filtrados por segurança
- Use apenas letras, números e acentos básicos

### Logs e Debug

Para ativar logs detalhados:
```bash
# Definir nível de log
export PYTHONPATH="${PYTHONPATH}:."
streamlit run main.py --logger.level=debug
```

### Suporte Técnico

Se o problema persistir:
1. Verifique se está usando Python 3.8+
2. Confirme se todas as dependências estão instaladas
3. Teste com uma entrada simples
4. Abra uma [issue](https://github.com/seu-usuario/gerador-planilhas-campo/issues) com detalhes do erro

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

### Resumo da Licença MIT:
- ✅ **Uso comercial** permitido
- ✅ **Modificação** permitida
- ✅ **Distribuição** permitida
- ✅ **Uso privado** permitido
- ❗ **Sem garantia** - uso por sua conta e risco

---

## 🏆 Reconhecimentos


### Tecnologias Utilizadas
- **Streamlit Team** - Framework excepcional para aplicações web em Python
- **ReportLab Team** - Biblioteca robusta para geração de PDFs
- **Python Community** - Linguagem e ecossistema fantásticos

### Agradecimentos Especiais
- Comunidade open source que torna projetos como este possíveis
- Usuários que contribuem com sugestões e melhorias

---

## 📞 Contato e Suporte

### **Pedro Higuchi** - Desenvolvedor Principal
- 💼 **LinkedIn**: [Pedro Higuchi](https://www.linkedin.com/in/pedro-higuchi-4085a81b/)
- 📧 **Email**: Disponível no LinkedIn
- 🐙 **GitHub**: [Seu GitHub](https://github.com/seu-usuario)

### Canais de Suporte
- 🐛 **Bugs**: [GitHub Issues](https://github.com/higuchip/gerador-planilhas-campo/issues)
- 💡 **Sugestões**: [GitHub Discussions](https://github.com/higuchip/gerador-planilhas-campo/discussions)
- 📚 **Documentação**: [Wiki do Projeto](https://github.com/higuchi/gerador-planilhas-campo/wiki)

### Sistema em Desenvolvimento
Este gerador faz parte de um **Sistema de Gerenciamento de Dados de Inventários de Florestas Nativas** mais amplo, atualmente em desenvolvimento. Fique ligado para futuras funcionalidades integradas!

---

## 📈 Estatísticas do Projeto

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/higuchip/gerador_planilha)
![GitHub contributors](https://img.shields.io/github/contributors/higuchip/gerador_planilha)
![GitHub issues](https://img.shields.io/github/issues/higuchip/gerador_planilha)
![GitHub pull requests](https://img.shields.io/github/issues-pr/higuchip/gerador_planilha)

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!**

**🌲 Contribua para o avanço da tecnologia florestal brasileira!**
