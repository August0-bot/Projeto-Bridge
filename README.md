#  Padrão de Projeto Bridge

Este repositório apresenta um estudo sobre o padrão de projeto **Bridge**, da categoria estrutural, com exemplos práticos, explicações e comparações entre o uso e a ausência do padrão.

##  Objetivo

O objetivo deste projeto é demonstrar como o padrão Bridge permite separar uma abstração da sua implementação, promovendo flexibilidade e facilitando a evolução independente de cada parte do sistema.

##  Conceito

> "Separar uma abstração da sua implementação, permitindo que ambas evoluam de forma independente."  
> — Gang of Four (GoF)

O Bridge é utilizado para evitar a explosão de subclasses em sistemas com múltiplas variações, como diferentes tipos de relatórios e formatos de exportação.

##  Problema Real

### Cenário:
Um sistema que gera diversos relatórios (financeiro, estoque, operacional) em múltiplos formatos (PDF, CSV, HTML).

### Sem Bridge:
Cada combinação exige uma nova classe:
- `RelatorioFinanceiroPDF`
- `RelatorioEstoqueCSV`
- `RelatorioOperacionalHTML`
- ...

### Com Bridge:
A separação em duas hierarquias independentes (Relatórios e Exportadores) permite combinações flexíveis e reutilização de código.

##  Exemplo com Bridge (resumo)

```python

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
```


##  Conclusão

O padrão Bridge ajuda a manter o sistema desacoplado, organizado e preparado para mudanças frequentes. Apesar da complexidade inicial, os benefícios em escalabilidade e manutenção compensam em sistemas de médio e grande porte.

##  Estrutura do Projeto

```
bridge-pattern/
│
├── sem_bridge.py          # Exemplo sem uso do padrão Bridge
├── com_bridge.py          # Exemplo completo utilizando o padrão Bridge
├── README.md              # Este arquivo

```

##  Autor

Desenvolvido por Augusto Martins como parte de um projeto acadêmico em Engenharia de Software.

---

📅 Apresentação: síncrona (24/06) ou vídeo (30/06)  
📘 Referência: GoF - Design Patterns: Elements of Reusable Object-Oriented Software
