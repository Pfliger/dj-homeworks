from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    ab_test_arg = request.GET.get('from-landing', None)
    if ab_test_arg == 'original':
        counter_click.update(['original'])
    elif ab_test_arg == 'test':
        counter_click.update(['test'])
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_test = request.GET.get('ab-test-arg', None)
    if ab_test == 'original':
        counter_show.update(['original'])
        return render(request, 'landing.html')
    elif ab_test == 'test':
        counter_show.update(['test'])
        return render(request, 'landing_alternate.html')



def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    result_original =counter_click['original'] / counter_show['original'] if counter_show['original'] else 0.0
    result_test = counter_click['test'] / counter_show['test'] if counter_show['test'] else 0.0
    return render(request, 'stats.html', context={
        'test_conversion': result_test,
        'original_conversion': result_original,
    })
