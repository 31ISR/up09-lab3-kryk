from django.shortcuts import render
# Импорт функции `render` из модуля `django.shortcuts`.
# Эта функция используется для отображения HTML-шаблонов
# с передачей в них данных.

def about(req):
    return render(req, "about.html")

def main(req):
    return render(req, 'index.html')
