from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'price')
        # fields = '__all__'  # Использование всех полей модели
        # fields = ('first_name',)  # Использование только перечисленных полей
        # exclude = ('last_name',)  # Использование всех полей, кроме перечисленных
        # Описан может быть только один из вариантов

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data.lower() in self.banned_words:
            raise ValidationError('Слова, запрещенные к использованию в названии продукта: казино, криптовалюта, '
                                  'крипта, биржа, дешево, бесплатно, обман, полиция, радар. ')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in self.banned_words:
            raise ValidationError('Слова, запрещенные к использованию в описании продукта: казино, криптовалюта, '
                                  'крипта, биржа, дешево, бесплатно, обман, полиция, радар. ')
        return cleaned_data
