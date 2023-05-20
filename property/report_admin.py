import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.contrib import admin
from reportlab.platypus import Table


def generate_property_report(modeladmin, request, queryset):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    
    # Set up table header
    table_header = ["Property Name", "Owner Name", "Price", "List Date", " Owner Id Number"]
    table_description = [table_header]
    
    # Write the report content
    for obj in queryset:
        # Add property details to the table description
        row = [obj.title, obj.owner.username, obj.price, obj.list_date, obj.owner.id_number]
        table_description.append(row)
        
        # Add inquiries to the table description
        for inquiry in obj.inquiries.all():
            row = ["", "", "", "", ""]
            table_description.append(row)
            row = ["", f"Client Name: {inquiry.name}", "", "", ""]
            table_description.append(row)
            row = ["", f"Phone Number: {inquiry.phone}", "", "", ""]
            table_description.append(row)
        
    # Draw the table
    table_style = [('GRID', (0, 0), (-1, -1), 0.5, (0, 0, 0)), ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 14)]
    table = Table(table_description, style=table_style)
    table.wrapOn(p, 800, 600)
    table.drawOn(p, 50, 500)
    
    # Set the filename of the PDF file
    filename = "property_report.pdf"
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    buffer.seek(0)
    # Create a new Django response object, and specify content_type as pdf
    response = FileResponse(buffer, content_type='application/pdf')
    # Set the Content-Disposition header to force download of the file
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

# Set the description and short description of the action
generate_property_report.short_description = "Generate Property Report"
generate_property_report.__name__ = "generate_property_report"
