from deep_translator import GoogleTranslator as gt

input_txt = input("번역할 한글을 입력하세요 : ")

# 번역과 관련된 Translate
# Google 번역을 통해 영어로 번역
# GoogleTranslator(source = 'auto', target = 'str')
translated = gt(source='ko', target='en').translate(input_txt)

print(f"입력한 한글 : {input_txt}\n번역된 영어 : {translated}")