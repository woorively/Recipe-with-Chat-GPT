# Recipe-with-Chat-GPT

## 🖇️ 참고 사항

### 1. Tools & Sources
- **OpenAI API**
- **Goorm IDE** : Integrated Development Environment
- **Django** : Python  Web Framework

### 2. Chat GPT API Example [🔗](https://platform.openai.com/examples)
- OpenAI API를 활용하여 만들 수 있는 서비스 예시

### 3. Chat GPT UI [🔗](https://platform.openai.com/playground)
**— 모델 사용 시 용어 의미**
- **temperature** : 예측을 할 때 모델의 신뢰도를 제어할 수 있는 0과 1 사이의 값으로, 온도를 낮추면 위험이 줄어들고 completion이 더 정확해진다. 온도를 높이면 더욱 다양하고 창의적인 completion을 얻을 수 있다.
- **Top p** : 텍스트 생성의 다양성과 정확성을 제어하는 데 사용되는 매개변수이다. 값이 작을수록 보다 일관된 답변을, 값이 클수록 보다 다양한 답변을 생성할 수 있다. 하지만 너무 작은 값은 모델의 답변을 지나치게 제한할 수 있고, 너무 큰 값은 모델의 답변을 지나치게 흐트러뜨릴 수 있으므로 적절한 값을 찾는 것이 중요하다.

### 4. OpenAI API Moderation [🔗](https://platform.openai.com/docs/guides/moderation/overview?lang=python)
- 콘텐츠가 OpenAI의 사용 정책을 준수하는지 확인하는 데 사용할 수 있는 도구
- 개발자는 사용 정책에서 금지하는 콘텐츠를 식별하고 필터링 등을 통해 조치
