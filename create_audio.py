from gtts import gTTS 
# This module is imported so that we can  
# play the converted audio 
# The text that you want to convert to audio 
toilet = 'I need to visit the lavatory'
water = 'I am feeling thirsty'
food = 'I am feeling hungry'
medical = 'I am feeling unwell'
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 

myobj = gTTS(text=toilet, lang=language, slow=False) 
myobj.save("toilet.mp3") 
 
myobj = gTTS(text=water, lang=language, slow=False) 
myobj.save("water.mp3") 

myobj = gTTS(text=food, lang=language, slow=False) 
myobj.save("food.mp3") 

myobj = gTTS(text=medical, lang=language, slow=False) 
myobj.save("medical.mp3") 

