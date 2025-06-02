import base64
import os
import tempfile
import uuid
import html
import re
import streamlit as st
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
import logging
from pathlib import Path

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurações de segurança
MAX_INPUT_LENGTH = 100
MAX_TREES = 2000
ALLOWED_CHARS = re.compile(r'^[a-zA-Z0-9\s\-_.áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ]+

def sanitize_input(text, max_length=MAX_INPUT_LENGTH):
    """Sanitiza entrada do usuário"""
    if not text:
        return ""
    
    # Limita tamanho
    text = str(text)[:max_length]
    
    # Remove caracteres perigosos
    if not ALLOWED_CHARS.match(text):
        # Remove caracteres não permitidos
        text = re.sub(r'[^a-zA-Z0-9\s\-_.áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ]', '', text)
    
    # Escapa HTML por segurança adicional
    text = html.escape(text)
    
    return text.strip()

def validate_number_input(value, min_val=0, max_val=MAX_TREES):
    """Valida entrada numérica"""
    try:
        num = int(value)
        if min_val <= num <= max_val:
            return num
        else:
            raise ValueError(f"Número deve estar entre {min_val} e {max_val}")
    except (ValueError, TypeError):
        raise ValueError("Entrada deve ser um número válido")

def create_secure_pdf(responsavel, area, n_trees):
    """Cria PDF de forma segura com arquivo temporário"""
    
    # Sanitiza entradas
    responsavel_safe = sanitize_input(responsavel)
    area_safe = sanitize_input(area)
    n_trees_safe = validate_number_input(n_trees)
    
    # Cria arquivo temporário seguro
    temp_dir = tempfile.mkdtemp()
    file_id = str(uuid.uuid4())
    pdf_path = os.path.join(temp_dir, f"planilha_campo_{file_id}.pdf")
    
    # Garante que o caminho é seguro
    temp_dir_resolved = Path(temp_dir).resolve()
    pdf_path_resolved = Path(pdf_path).resolve()
    if not str(pdf_path_resolved).startswith(str(temp_dir_resolved)):
        raise ValueError("Caminho de arquivo inseguro")
    
    try:
        # Configurações do PDF
        styles = getSampleStyleSheet()
        colwidths = [0.5 * inch, 0.5 * inch, 2 * inch, 1.5 * inch, 0.5 * inch, 1.5 * inch]
        
        def header(canvas, pdf):
            """Header seguro do PDF"""
            # Limita tamanho do texto no canvas
            canvas.drawString(165, 800, "PLANILHA DE CAMPO - INVENTÁRIO FLORESTAL")
            canvas.drawString(63, 765, f"ÁREA: {area_safe[:50]}")  # Limita tamanho
            canvas.drawString(410, 765, "DATA:_____________")
            canvas.drawString(63, 745, f"RESPONSÁVEL: {responsavel_safe[:40]}")  # Limita tamanho
            canvas.drawString(290, 745, "EQUIPE:_____________________________")
            page_num = canvas.getPageNumber()
            text = f"Página {page_num}"
            canvas.drawRightString(530, 30, text)
        
        # Cria PDF
        pdf = BaseDocTemplate(pdf_path, pagesize=A4)
        frame = Frame(
            pdf.leftMargin - inch * 0.5,
            pdf.bottomMargin,
            pdf.width + inch,
            pdf.height - inch * 0.5,
        )
        template = PageTemplate(id="all_pages", frames=frame, onPage=header)
        pdf.addPageTemplates([template])
        
        # Dados da tabela
        data = [["Parc.", "Núm.", "Espécie", "CAP/DAP", "Alt.", "Obs"]]
        data.extend([[" ", " ", " ", " ", " ", " "] for i in range(n_trees_safe)])
        
        # Estilos da tabela
        table_style = TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.25, colors.gray),
            ("ALIGN", (2, 0), (4, -1), "CENTER"),
        ])
        
        table = Table(data, repeatRows=1, style=table_style, colWidths=colwidths)
        pdf.build([table])
        
        logger.info(f"PDF criado com sucesso: {n_trees_safe} árvores")
        return pdf_path
        
    except Exception as e:
        logger.error(f"Erro ao criar PDF: {e}")
        # Limpa arquivo se houve erro
        if os.path.exists(pdf_path):
            try:
                os.remove(pdf_path)
            except:
                pass
        raise

def get_secure_download_link(file_path, display_name="planilha_campo.pdf"):
    """Cria link de download seguro"""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        
        bin_str = base64.b64encode(data).decode()
        
        # Nome de arquivo sanitizado
        safe_filename = sanitize_input(display_name.replace('.pdf', '')) + '.pdf'
        
        href = f'<a href="data:application/pdf;base64,{bin_str}" download="{safe_filename}">📥 Download Planilha PDF</a>'
        return href
        
    except Exception as e:
        logger.error(f"Erro ao criar link de download: {e}")
        return "<p>❌ Erro ao gerar download</p>"
    
    finally:
        # Limpa arquivo temporário
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                # Remove diretório temporário se vazio
                parent_dir = os.path.dirname(file_path)
                if os.path.exists(parent_dir) and not os.listdir(parent_dir):
                    os.rmdir(parent_dir)
        except Exception as cleanup_error:
            logger.warning(f"Erro na limpeza: {cleanup_error}")

# Interface Streamlit segura
st.set_page_config(
    page_title="Gerador de Planilhas de Campo",
    page_icon="📝",
    layout="centered"
)

st.title("Gerador de Planilhas de Campo para Inventários Florestais 📝")

st.markdown("""
**Planilhas de campo** são itens obrigatórios no check-list para a realização de inventários 
florestais. Por mais simples que seja a sua preparação, os contratempos podem ser vários, como uma eventual 
necessidade de urgência e a perda/corrompimento do arquivo no computador.

Tendo em vista a praticidade e agilidade de um processo automatizado, aqui apresento um **Gerador de Planilhas de 
Campo** padronizadas. Após o preenchimento das informações abaixo, clique em 'Gerar PDF' 
para obtenção de seu arquivo pronto para impressão.
""")

st.markdown("---")

# Seção 1: Responsável Técnico
st.markdown("### 1️⃣ Responsável Técnico")
responsavel = st.text_input(
    "Nome do responsável técnico:",
    max_chars=MAX_INPUT_LENGTH,
    help="Apenas letras, números, espaços e acentos são permitidos"
)

# Seção 2: Área
st.markdown("### 2️⃣ Identificação da Área")
area = st.text_input(
    "Nome ou código da área:",
    max_chars=MAX_INPUT_LENGTH,
    help="Apenas letras, números, espaços e acentos são permitidos"
)

# Seção 3: Número de árvores
st.markdown("### 3️⃣ Configuração da Planilha")
n_arvores = st.number_input(
    "Número de árvores a serem medidas:",
    min_value=1,
    max_value=MAX_TREES,
    value=50,
    step=1,
    help=f"Máximo {MAX_TREES} árvores por planilha"
)

# Validação e geração
st.markdown("---")

if st.button("🔄 Gerar Planilha PDF", type="primary"):
    if not responsavel.strip():
        st.error("❌ Nome do responsável é obrigatório")
    elif not area.strip():
        st.error("❌ Identificação da área é obrigatória")
    else:
        try:
            with st.spinner("📄 Gerando planilha..."):
                # Cria PDF seguro
                pdf_path = create_secure_pdf(responsavel, area, n_arvores)
                
                # Gera link de download
                download_link = get_secure_download_link(pdf_path)
                
                st.success("✅ Planilha gerada com sucesso!")
                st.markdown("### 4️⃣ Download")
                st.markdown(download_link, unsafe_allow_html=True)
                
                # Informações da planilha gerada
                st.info(f"""
                📋 **Planilha gerada:**
                - **Responsável**: {sanitize_input(responsavel)}
                - **Área**: {sanitize_input(area)}
                - **Árvores**: {n_arvores}
                """)
                
        except ValueError as ve:
            st.error(f"❌ Erro de validação: {ve}")
        except Exception as e:
            st.error("❌ Erro ao gerar planilha. Tente novamente.")
            logger.error(f"Erro na geração: {e}")

# Informações adicionais
st.markdown("---")
st.markdown("### 📞 Contato")
st.markdown("""
**Desenvolvido por Pedro Higuchi**  
🔗 [LinkedIn](https://www.linkedin.com/in/pedro-higuchi-4085a81b/)

**Observação**: Sistema em desenvolvimento para incorporação no 
***Sistema de Gerenciamento de Dados de Inventários de Florestas Nativas***.
""")

# Contador de uso seguro (por sessão)
if 'page_views' not in st.session_state:
    st.session_state.page_views = 1
else:
    st.session_state.page_views += 1

st.caption(f"Sessão atual: {st.session_state.page_views} interações")
