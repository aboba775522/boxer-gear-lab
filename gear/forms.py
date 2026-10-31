from django import forms

class QuizForm(forms.Form):
    weight = forms.IntegerField(
        label="Твой вес (кг)",
        min_value=40,
        max_value=150,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Например, 75'})
    )
    EXPERIENCE_CHOICES = [
        ('beginner', 'Новичок (0-1 год)'),
        ('intermediate', 'Уверенный любитель (1-3 года)') ,
        ('pro', 'Профессионал / Опытный (3+ лет)'),
    ]
    experience = forms.ChoiceField(
        label="Уровень подготовки",
        choices=EXPERIENCE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    budget = forms.IntegerField(
        label="Бюджет на покупку (руб.)",
        min_value=1000,
        max_value=100000,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Например, 10000'})
    )