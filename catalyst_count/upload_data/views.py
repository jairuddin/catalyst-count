from django.shortcuts import render, redirect
from django.http import JsonResponse
import os
from .models import File
from django.contrib.auth.decorators import login_required
import csv
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.db import transaction


@login_required
def index(request):
    if request.method == 'POST': 
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file uploaded'})
        
        file = request.FILES['file']

        # Ensure the 'media' directory exists
        media_dir = 'media'
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)

        temp_path = os.path.join(media_dir, file.name)

        # Save the uploaded file
        with open(temp_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        try:
            chunk_size = 10000  # Adjust the chunk size based on your needs
            with open(temp_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                batch = []
                for row in reader:
                    # Access each field from the CSV row
                    emp = row.get('')  # Ensure this matches your CSV structure
                    name = row.get('name')
                    domain = row.get('domain')
                    year_founded = row.get('year founded')
                    industry = row.get('industry')
                    size_range = row.get('size range')
                    locality = row.get('locality')
                    country = row.get('country')
                    linkedin_url = row.get('linkedin url')
                    current_employee_estimate = row.get('current employee estimate')
                    total_employee_estimate = row.get('total employee estimate')

                    # Prepare data for bulk insertion
                    company = File(
                        emp=emp,
                        name=name,
                        domain=domain,
                        year_founded=int(float(year_founded)) if year_founded else None,
                        industry=industry,
                        size_range=size_range,
                        locality=locality,
                        country=country,
                        linkedin_url=linkedin_url,
                        current_employee_estimate=int(current_employee_estimate) if current_employee_estimate else None,
                        total_employee_estimate=int(total_employee_estimate) if total_employee_estimate else None,
                    )
                    batch.append(company)

                    if len(batch) >= chunk_size:
                        with transaction.atomic():
                            File.objects.bulk_create(batch)
                        batch = []

                if batch:
                    with transaction.atomic():
                        File.objects.bulk_create(batch)

            messages.success(request, 'File uploaded and processed successfully.')
            return render(request, 'file_upload/index.html')
        
        except Exception as e:
            return JsonResponse({'error': str(e)})
    
    return render(request, 'file_upload/index.html')


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('account_login')
