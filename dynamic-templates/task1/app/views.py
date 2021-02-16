from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', mode='rt', encoding='utf-8') as data_file:
        columns = data_file.readline().strip().split(';')
    with open('inflation_russia.csv', mode='rt', encoding='utf-8') as data_file:
        reader = csv.DictReader(data_file, delimiter=';')
        data = []
        for item in reader:
            for column in columns[1:]:
                try:
                    item[column] = float(item[column])
                except ValueError:
                    item[column] = '-'
            data.append(item)
    context = {'columns': columns, 'data': data}
    return render(request, template_name, context)
