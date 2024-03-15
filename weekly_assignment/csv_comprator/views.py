from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify
from datetime import datetime  # Importing datetime function from datetime module
from .forms import UploadFileForm
from .utils import find_corrections

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file1 = request.FILES['file1']
            file2 = request.FILES['file2']
            comparison_result = find_corrections(file1, file2)
            
            # Generate a CSV file content from the comparison result
            csv_content = '\n'.join([f'{location},{actual_value},{incorrect_value}' for location, actual_value, incorrect_value in comparison_result])
            
            # Create a unique filename based on the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f'corrections_{slugify(timestamp)}.csv'
            
            # Create the HTTP response with CSV content as attachment
            response = HttpResponse(csv_content, content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    else:
        form = UploadFileForm()
    return render(request, 'csv_comprator/upload_file.html', {'form': form})



