import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import core
import os
import webbrowser

import openai 
from get_env import print_env

key = openai.api_key
env = print_env(['app_key'])

#configura ambeinte
openai.api_key = env['app_key']

# model_engine 
model_engine = 'text-davinci-003'

audio = sr.Recognizer()
maquina = pyttsx3.init()

def listen_command():
    try:
        with sr.Microphone() as source:
            print('Escutando..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'jarvis' in comando:
                comando = comando.replace('jarvis', '')
                maquina.say(comando)
                maquina.runAndWait()

    except Exception as e:
        print(f'Microfone não está ok {e}')
    # print(f'o comando é: {comando}')
    return comando
    
    
            
def execute_command():
    comando = listen_command()
    if 'procure por' in comando or 'qual o significado' in comando or 'o que significa' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say(f'Tocando {musica} no youtube!')
        maquina.runAndWait()
    elif 'que horas são' in comando:
        maquina.say(core.SystemInfo.get_time())
        maquina.runAndWait()
    elif 'abra o google chrome' in comando:
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        maquina.say('abrindo Google Chrome')
        maquina.runAndWait()
    
    # elif 'responda' in comando or 'fale sobre' in comando or 'crie' in comando or 'o que você acha sobre' in comando:
    #     prompt = comando.replace('responda','')
    #     completion = openai.Completion.create(
    #         engine = model_engine,
    #         prompt = prompt,
    #         max_tokens = 1024,
    #         temperature = 0.5,
    #     )
    #     reponse = completion.choices[0].text
    #     print(reponse)
    #     maquina.say(reponse)
    #     maquina.runAndWait()
        
while True:
    execute_command()