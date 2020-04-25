import speech_recognition as sr
import webbrowser as wb

print(" HEY EVERYONE")
print(" SEARCH ANYTHING FROM GOOGLE ,YOUTUBE AND GOTO THE MYCAPTAIN PAGE AS WELL  ")
print(" SAY ANYTHING AND FIND YOUR RESULT")
r1= sr.Recognizer()
r2= sr.Recognizer()
r3= sr.Recognizer()
r4= sr.Recognizer()

with sr.Microphone() as source:
    print('[search youtube: search google]')
    print("Say hello & Go to mycaptain page")
    print('speak now')
    audio = r3.listen(source)



if 'video' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url= 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)

        try:
            get= r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

            
if 'hi' in r4.recognize_google(audio):
    r4 = sr.Recognizer()
    url= 'https://www.google.com/search?q='
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)

        try:
            get= r4.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))


if 'hello' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url= 'https://www.mycaptain.in/'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)

        try:
            get= r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))


