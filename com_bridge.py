
class Exportador:
    def exportar(self, conteudo): pass

class PDFExportador(Exportador):
    def exportar(self, conteudo):
        print(f"Exportando em PDF:\n{conteudo}")

class CSVExportador(Exportador):
    def exportar(self, conteudo):
        print(f"Exportando em CSV:\n{conteudo}")

class Relatorio:
    def __init__(self, exportador: Exportador):
        self.exportador = exportador
        self.titulo = ""
        self.conteudo = []

    def adicionar_dado(self, dado):
        self.conteudo.append(dado)

    def gerar(self):
        dados_formatados = f"{self.titulo}\n" + "\n".join(self.conteudo)
        self.exportador.exportar(dados_formatados)

class RelatorioFinanceiro(Relatorio):
    def __init__(self, exportador):
        super().__init__(exportador)
        self.titulo = "Relatório Financeiro"

class RelatorioEstoque(Relatorio):
    def __init__(self, exportador):
        super().__init__(exportador)
        self.titulo = "Relatório de Estoque"

if __name__ == "__main__":
    rf = RelatorioFinanceiro(PDFExportador())
    rf.adicionar_dado("Receita: R$ 10.000")
    rf.adicionar_dado("Despesas: R$ 7.000")
    rf.gerar()

    re = RelatorioEstoque(CSVExportador())
    re.adicionar_dado("Produto A: 100 unidades")
    re.adicionar_dado("Produto B: 50 unidades")
    re.gerar()
