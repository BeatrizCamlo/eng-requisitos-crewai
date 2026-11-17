from crewai.tools import BaseTool
from pypdf import PdfReader
import os

class LerPdfTool(BaseTool):
    name: str = "Ler PDF Completo"
    description: str = "Lê e extrai todo o texto de um arquivo PDF dado o seu caminho no repositório."

    def _run(self, caminho_arquivo: str) -> str:
        if not os.path.exists(caminho_arquivo):
            return f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado no caminho especificado."
        
        try:
            reader = PdfReader(caminho_arquivo)
            texto = ""
            for i, page in enumerate(reader.pages):
                extracted = page.extract_text()
                if extracted:
                    texto += f"--- Página {i+1} ---\n" + extracted + "\n\n"
            return texto if texto else "O PDF está vazio ou não contém texto legível."
        except Exception as e:
            return f"Erro ao ler o arquivo PDF: {str(e)}"