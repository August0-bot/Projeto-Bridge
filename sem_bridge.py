
class RelatorioFinanceiroPDF:
    def gerar(self):
        print("Gerando relatório financeiro em PDF")

class RelatorioEstoqueCSV:
    def gerar(self):
        print("Gerando relatório de estoque em CSV")


if __name__ == "__main__":
    rf = RelatorioFinanceiroPDF()
    rf.gerar()

    re = RelatorioEstoqueCSV()
    re.gerar()
