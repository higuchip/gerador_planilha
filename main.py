import base64
import os
from reportlab.platypus import BaseDocTemplate
from reportlab.platypus import Frame, PageTemplate
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
import streamlit as st

st.title("Gerador de Planilhas de Campo para Inventários Florestais 📝")

st.write(
    "Planilhas de campo são itens obrigatórios no check-list para a realização de inventários "
    "florestais. Por mais simples que seja a sua preparação, os contratempos podem ser vários, como uma eventual "
    "necessidade de urgência e a perda/corrompimento do arquivo no computador."
)

st.write(
    "Tendo em vista a praticidade e agilidade de um processo automatizado, aqui apresento um Gerador de Planilhas de "
    "Campo padronizadas. Após o preenchimento das informações abaixo, clique em 'Download' "
    "para obtenção de seu arquivo no formato PDF pronto para impressão."
)

st.write()


st.write("### 1) Indicação do Responsável Técnico")
RESPONSAVEL = st.text_input("Digite o nome do responsável técnico pelo levantamento:")

st.write("### 2) Indicação da Área")
AREA = st.text_input(
    "Digite o nome ou código da área onde será realizado o inventário florestal:"
)

st.write("### 3) Definição do tamanho da planilha")
N_ARV = st.number_input(
    "Insira o número de árvores que potencialmente serão medidas:", min_value=0, step=1
)

# Geração do PDF

styles = getSampleStyleSheet()
colwidths = [0.5 * inch, 0.5 * inch, 2 * inch, 1.5 * inch, 0.5 * inch, 1.5 * inch]


def header(canvas, pdf):
    canvas.drawString(165, 800, "PLANILHA DE CAMPO - INVENTÁRIO FLORESTAL")
    canvas.drawString(63, 765, f"ÁREA: {AREA}")
    # canvas.setLineWidth(inch * 0.01)
    # canvas.line(100, 760, 200, 760)
    canvas.drawString(410, 765, "DATA:_____________")
    canvas.drawString(63, 745, f"RESPONSÁVEL: {RESPONSAVEL}")
    canvas.drawString(290, 745, "EQUIPE:_____________________________")
    page_num = canvas.getPageNumber()
    text = "Página %s" % page_num
    canvas.drawRightString(530, 30, text)


pdf = BaseDocTemplate("planilha_campo.pdf", pagesize=A4)
frame = Frame(
    pdf.leftMargin - inch * 0.5,
    pdf.bottomMargin,
    pdf.width + inch,
    pdf.height - inch * 0.5,
)
# showBoundary=1)  # Delete to remove line around the frame.
template = PageTemplate(id="all_pages", frames=frame, onPage=header)
pdf.addPageTemplates([template])
# Data for table
data = [["Parc.", "Núm.", "Espécie", "CAP/DAP", "Alt.", "Obs"]]
data.extend([[" ", " ", " ", " ", " ", " "] for i in range(N_ARV)])
# Styles for table
table_style = TableStyle(
    [
        ("GRID", (0, 0), (-1, -1), 0.25, colors.gray),
        # ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
        ("ALIGN", (2, 0), (4, -1), "CENTER"),
    ]
)
# Create table and repeat row 1 at every split.
table = Table(data, repeatRows=1, style=table_style, colWidths=colwidths)
pdf.build([table])


# From GokulNC in https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806/26 (Thanks!)
def get_binary_file_downloader_html(bin_file, file_label="File"):
    with open(bin_file, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download</a>'
    return href


st.write("### 4) Baixar o arquivo PDF da planilha")
st.markdown(
    get_binary_file_downloader_html("planilha_campo.pdf", "Planilha"),
    unsafe_allow_html=True,
)
st.write("### Contato:")
st.write(
    "Desenvolvido por ***Pedro Higuchi***. Em caso de dúvidas ou outras informações entre em [contato] (https://www.linkedin.com/in/pedro-higuchi-4085a81b/)."
)
st.write(
    "Observação: Funcionalidade em teste para posteriormente ser incorporado no ***Sistema de Gerenciamento "
    "de Dados de Inventários de Florestas Nativas***, em desenvolvimento."
)


@st.cache(allow_output_mutation=True)
def Pageviews():
    return []


pageviews = Pageviews()
pageviews.append("dummy")

try:
    st.markdown("Contador de visitas: {}".format(len(pageviews)))
except ValueError:
    st.markdown("Contador de visitas: {}".format(1))
