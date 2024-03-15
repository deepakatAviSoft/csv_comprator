from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .utils import compare_csv_files

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file1 = request.FILES['file1']
            file2 = request.FILES['file2']
            comparison_result = compare_csv_files(file1, file2)
            return render(request, 'csv_comprator/comparison_result.html', {'comparison_result': comparison_result})
    else:
        form = UploadFileForm()
    return render(request, 'csv_comprator/upload_file.html', {'form': form})
