from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import tempfile

def generate_pdf_report(template_name, context):
    """
    Gera um PDF a partir de um template HTML
    """
    html_string = render_to_string(template_name, context)
    
    with tempfile.NamedTemporaryFile(suffix='.pdf') as output:
        HTML(string=html_string).write_pdf(output.name)
        
        with open(output.name, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="report.pdf"'
            return response

def format_currency(value):
    """
    Formata valor monetário
    """
    return f'R$ {value:,.2f}'

def get_date_range_filter(start_date, end_date, field_name):
    """
    Retorna filtro de intervalo de datas
    """
    date_filter = {}
    if start_date:
        date_filter[f'{field_name}__gte'] = start_date
    if end_date:
        date_filter[f'{field_name}__lte'] = end_date
    return date_filter
