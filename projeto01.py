projeto = input("Qual o nome do Projeto?: ")
horas_previstas = (input('Quantas horas previstas?: '))
valor_hora = (input("Qual o valor por hora?: "))
prazo = (input("Qual o prazo previsto?: "))
valor_total = int(horas_previstas) * float(valor_hora)

from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial')
pdf.image("meu template.png", x=0, y=0)

pdf.text(115, 192, projeto)
pdf.text(115, 207, horas_previstas)
pdf.text(115, 219, valor_hora)
pdf.text(115, 232, prazo)
pdf.text(115, 245, str(valor_total))

pdf.output("Orçamento.pdf")
print('Orçamento gerado com sucesso!')