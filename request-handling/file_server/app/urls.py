
from datetime import datetime, date
from django.urls import path, converters, register_converter
from app.views import file_list, file_content


# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, self.format).date()

    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format)


register_converter(DateConverter, 'date')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<date:date>/', file_list, name='file_list'),
    path('<str:name>/', file_content, name='file_content')
]
