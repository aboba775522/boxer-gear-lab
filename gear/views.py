import pandas as pd
from django.shortcuts import render
from .forms import QuizForm
from .models import EquipmentItem

def quiz_view(request):
    recommendations = None
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            budget = form.cleaned_data['budget']
            experience = form.cleaned_data['experience']

            # Достаем все товары из базы данных в виде списка словарей
            items_qs = EquipmentItem.objects.all().values(
                'id', 'name', 'brand', 'price', 'category__name', 'affiliate_link', 'image_url', 'description'
            )
            
            if items_qs.exists():
                # Превращаем данные в DataFrame для аналитической фильтрации через Pandas
                df = pd.DataFrame(list(items_qs))

                df_filtered = df[df['price'] <= budget]

                # Логика ранжирования/подбора в зависимости от веса и опыта (пример аналитики)
                if not df_filtered.empty:
                    recommendations = df_filtered.to_dict(orient='records')
            
            #сохраняем результаты в сессию
            request.session['quiz_data'] = {
                'weight': weight,
                'budget': budget,
                'experience': experience
            }
    else:
        form = QuizForm()

    context = {
        'form': form,
        'recommendations': recommendations,
    }
    return render(request, 'gear/quiz.html', context)