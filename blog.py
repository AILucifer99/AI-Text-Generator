import openai
import config
from utils import parseGenerationTokens as genToken
from utils import parseTemperature as genTemp

openai.api_key = config.OPENAI_API_KEY


def generateBlogTopics(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Generate blog topics on: {}. \n \n 1.  ".format(prompt1),
      temperature=genTemp.TemperatureSynthesizer(True),
      max_tokens=genToken.GenerationTokenSynthesizer(True, 75, 150, 20),
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response['choices'][0]['text']

def generateBlogSections(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog title in to high level blog sections: {} \n\n- Introduction: ".format(prompt1),
      temperature=genTemp.TemperatureSynthesizer(True),
      max_tokens=genToken.GenerationTokenSynthesizer(True, 85, 165, 20),
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response['choices'][0]['text']


def blogSectionExpander(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog section in to a detailed professional, witty and clever explanation.\n\n {}".format(prompt1),
      temperature=genTemp.TemperatureSynthesizer(True),
      max_tokens=genToken.GenerationTokenSynthesizer(True, 575, 900, 5),
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response['choices'][0]['text']
