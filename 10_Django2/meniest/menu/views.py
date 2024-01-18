from django.shortcuts import render, redirect
from django.conf import settings
from .models import UserRequest, TranslationResponse
import deepl
from .forms import TranslationForm
from django.http import HttpResponse
from django.template import loader

auth_key = settings.DEEPL_API_KEY
translator = deepl.Translator(auth_key)
lang_list = ['EN-US','ZH','KO']

def index(request):
    
    result = {}
    
    if request.method == "POST":
        form = TranslationForm(request.POST)
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            for lang in lang_list:
                result[lang] = translator.translate_text(sentence, target_lang=lang).text
    else:
        form = TranslationForm()
    context = {
        'form': form,
        'result': result
    }
    return render(request, 'menu/index.html', context)


# def translate_request(request):
#     if request.method == "POST":
#         # フォームからテキスト入力を取得
#         input_text = request.POST.get('input_text')

#         # UserRequest モデルにユーザーのリクエストを保存
#         user_request = UserRequest.objects.create(input_text=input_text)

#         lang_list = ['EN-US','ZH']
#         for lang in lang_list:
#             response = translator.translate_text(input_text, target_lang=lang)
#             TranslationResponse.objects.create(
#                 request=user_request,
#                 translated_text=response,
#                 language=lang
#             )    

#         # 完了ページまたは結果ページにリダイレクト
#         return redirect('translation_complete')

#     # POSTリクエストでない場合は、通常のフォームを表示
#     return render(request, 'translate_form.html')
