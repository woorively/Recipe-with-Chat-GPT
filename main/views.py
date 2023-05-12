from django.shortcuts import render

import openai
import os
import random

openai.api_key = "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"  # OpenAI API 키를 입력하세요

def recipe_generator(request):
    if request.method == 'POST':
        ingredient_list = request.POST.get('ingredients').split(', ')
        lst = get_ingredient(ingredient_list)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"주어진 재료 : {','.join(lst)} 어떤 음식을 만들 수 있어? 단계에 따라 알려줘. 그리고, 첫 줄에 음식의 이름을 말해줘.",
            max_tokens=500,
            temperature=0.6
        )

        output = response['choices'][0]['text'].strip('\n')
        output_list = output.split("\n")
        title = output_list[0]
        instructions = '\n'.join(output_list[1:])

        return render(request, 'recipe.html', {'title': title, 'instructions': instructions, 'ingredients': lst})

    return render(request, 'index.html')

def get_ingredient(ingredient_list):
    ingredient_lst = []

    for _ in range(0, 3):
        ingredient_lst.append(
            ingredient_list[random.randint(0, len(ingredient_list)-1)])

    return ingredient_lst

