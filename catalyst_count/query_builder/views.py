from django.shortcuts import render
from django.views import View
import requests

class FilterFormView(View):
    template_name = 'query_builder_temp/filter_form.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 

    def post(self, request, *args, **kwargs):
        
        industry = request.POST.get('industry', '').strip()
        locality = request.POST.get('locality', '').strip()
        country = request.POST.get('country', '').strip()
        year_founded = request.POST.get('year_founded', '').strip()
        

        params = {
            
            'industry': industry if industry else None,
            'locality': locality if locality else None,
            'country': country if country else None,
            'year_founded': year_founded if year_founded else None,
        }
        
        params = {k: v for k, v in params.items() if v is not None}
        
        try:
            response = requests.get('http://127.0.0.1:8000/filter/', params=params)
            response.raise_for_status()
            data = response.json()
            count = data.get('count', 'Error fetching count')
        except requests.exceptions.RequestException as e:
            count = f"Error fetching count: {e}"
        
        
        
        return render(request, self.template_name, {'count': count})
