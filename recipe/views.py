from django.shortcuts import render

import openai
import random

openai.api_key = "OpenAI_API_KEY" 

def recipe_generator(request):
    if request.method == 'POST':        
        lst = request.POST.get('ingredients').split(', ')

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"주어진 재료 : {', '.join(lst)}로 어떤 음식을 만들 수 있어? 단계에 따라 알려줘. 그리고, 첫 줄에 음식의 이름을 말해줘.",
            max_tokens=500,
            temperature=0.6
        )

        output = response['choices'][0]['text'].strip('\n')
        output_list = output.split("\n")
        title = output_list[0]
        instructions = '\n'.join(output_list[1:])

        return render(request, 'recipe.html', {'title': title, 'instructions': instructions, 'ingredients': lst})

    return render(request, 'index.html')
