from django.shortcuts import render, redirect
from django.conf import settings
from .models import UserRequest, TranslationResponse
# 英語と中国語の翻訳用にChatGptAPIをインポート
from .deepl import translator_deepl #これを実装する

auth_key = settings.DEEPL_API_KEY

def translate_request(request):
    if request.method == "POST":
        # フォームからテキスト入力を取得
        input_text = request.POST.get('input_text')

        # UserRequest モデルにユーザーのリクエストを保存
        user_request = UserRequest.objects.create(input_text=input_text)

        lang_list = ['EN-US','ZH']
        for lang in lang_list:
            response = translator_deepl(text=input_text, lang=lang, key=auth_key)
            TranslationResponse.objects.create(
                request=user_request,
                translated_text=response,
                language=lang
            )    

        # 完了ページまたは結果ページにリダイレクト
        return redirect('translation_complete')

    # POSTリクエストでない場合は、通常のフォームを表示
    return render(request, 'translate_form.html')
