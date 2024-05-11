#Configurações iniciais
import google.generativeai as genai
import textwrap
from IPython.display import display
from IPython.display import Markdown


GOOGLE_API_KEY="AIzaSyDukGM-no2DpLmBDGJZsKptJWnn2U1p21Y"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}

safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
    }

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)
response = model.generate_content("Que empresa criou o modelo de IA Gemini?")
response.text

print('''Crie a viagem dos seus sonhos com a Nomad Travel

Cansado de perder horas pesquisando destinos e roteiros de viagem? A Nomad Travel te ajuda a realizar a viagem dos seus sonhos com praticidade e exclusividade!

✈️ Escolha seu destino e deixe o roteiro por nossa conta!
  Como funciona?

Preencha as informações abaixo e receba seu roteiro personalizado imediatamente.

1.   Escolha seu destino: Sonha em conhecer as paisagens paradisíacas do Caribe? Explorar as milenares pirâmides do Egito? Ou se aventurar pelas trilhas do Machu Picchu? O destino é seu!
2.   Nos conte sobre você: Quais são seus interesses? Qual o seu estilo de viagem? Relaxante, aventureiro, cultural? Quanto tempo você tem disponível? Quanto mais informações você nos fornecer, mais personalizado será o seu roteiro.

  ''')

chat = model.start_chat()
destino = input('Escolha Seu Destino: ')
informacoes = input('nos conte sobre voce: ')
while destino != "fim":
  response = chat.send_message(f'faça um roteiro de viagem para: {destino}, com essas informações: {informacoes}')
  print("Esse é o roteiro personalizado para sua viagem:", response.text, '\n\n')
  destino = input('Escolha Seu Destino: ')
  informacoes = input('nos conte sobre voce: ')