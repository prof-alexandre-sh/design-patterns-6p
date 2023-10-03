'''
Exercício em sala

Implemente um exemplo usando o Abs. Factory onde necessitamos
gerar relatório em dois formatos diferentes, PDF e CSV.

O client poderá chamar qualquer uma das duas fábricas e chamar a função
que gera o relatório
'''

from abc import ABC, abstractmethod

# Classe abstrata para a fábrica abstrata de relatórios
class ReportFactory(ABC):
    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_footer(self):
        pass

# Fábrica concreta para criar relatórios em formato PDF
class PDFReportFactory(ReportFactory):
    pass

# Fábrica concreta para criar relatórios em formato CSV
class CSVReportFactory(ReportFactory):
    pass

# Classe abstrata para o cabeçalho do relatório
class ReportHeader(ABC):
    pass

# Implementação do cabeçalho em formato PDF
class PDFHeader(ReportHeader):
    pass

# Implementação do cabeçalho em formato CSV
class CSVHeader(ReportHeader):
    pass

# Classe abstrata para o corpo do relatório
class ReportBody(ABC):
    pass

# Implementação do corpo em formato PDF
class PDFBody(ReportBody):
    pass

# Implementação do corpo em formato CSV
class CSVBody(ReportBody):
    pass

# Classe abstrata para o rodapé do relatório
class ReportFooter(ABC):
    pass

# Implementação do rodapé em formato PDF
class PDFFooter(ReportFooter):
    pass

# Implementação do rodapé em formato CSV
class CSVFooter(ReportFooter):
    pass

# Função para criar um relatório completo usando a fábrica
def create_report(factory):
    pass

# Cliente
def main():
    pdf_report = create_report(PDFReportFactory())
    csv_report = create_report(CSVReportFactory())

    print("Relatório em PDF:")
    print(pdf_report)

    print("\nRelatório em CSV:")
    print(csv_report)

if __name__ == "__main__":
    main()