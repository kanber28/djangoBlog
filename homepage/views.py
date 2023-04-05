from django.shortcuts import render
from models import Post


def create_example_record(request):
    data = Post(title='deneme Başlık', content='deneme uzun sayılabilecek kontent')
    data.save()
