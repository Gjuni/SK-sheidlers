## RSS 서비스를 이용하여 매일 정보를 수집해서 이슈를 확인하려고함.
## 음성으로 변환해서 저장해서 들을 예정

# 조건
## feedparser : RSS 서비스 정보 가져오기
## gTTS : 음성 변환 라이브러리
## 요약 내용 부분을 음성으로 변환

# 가이드
## 파싱을 이용해서 보안뉴스나 데일리시큐 RSS 정보 중에서 요약 부분을 가져온다.
## 가져온 요약 정보를 gTTS를 이용해서 mp3 파일로 생성 및 저장.

import feedparser as fp
from gtts import gTTS

titles= []
descriptions = []
feed_url = "https://www.boannews.com/media/news_rss.xml"

## rss 함수
def rss_function() :
    parse_rss = fp.parse(feed_url)

    for entry in parse_rss.entries: # entry가 가장 상위이기 때문에 .entries
        titles.append(entry.title)
        descriptions.append(entry.description) ## dictionary 형태로 존재. tag값을 가져옴

def tts_function() :
    text = []

    for index, (title, desc) in enumerate(zip(titles, descriptions)):
        text.append(f"{index}: {title}\n{desc}\n")
        
        if index >= 5:
            break

    all_text = "\n".join(text)

    tts = gTTS(text= all_text, lang= 'ko', slow=False)
    print(text)

    tts.save('02_PBL_TTS.mp3')


def main():
    rss_function()
    tts_function()


if __name__ == "__main__":
    main()