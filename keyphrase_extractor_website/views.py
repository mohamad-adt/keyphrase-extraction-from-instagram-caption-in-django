from django.shortcuts import render
from extraction_files import KeyphraceExtraction
from extraction_files import GetDiscription_Bot

def home_page(request):
    username = ''
    result = ''
    key_phraces = ''
    if request.method == "POST":
        username = request.POST.get('getUsername')
        document = GetDiscription_Bot.main(UsrName=username)
        key_phraces = KeyphraceExtraction.main(document=document)
        for item in key_phraces:
            result += item+'\n'

    context = {
        "result": result
    }

    return render(request, "Home_page.html", context)