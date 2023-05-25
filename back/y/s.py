def po(name,model):

 import tensorflow as tf
 import pandas as pd
 import random
 import json
 with open('y/intents.json') as json_data:

  data1= json.load(json_data)
 tags=[]
 inputs=[]
 responses={}
 for intent in data1['intents']:
  responses[intent['tag']]=intent['responses']
  for l in intent['patterns']:
    inputs.append(l)
    tags.append(intent['tag'])

 data=pd.DataFrame({"patterns":inputs,"tags":tags})
 data=data.sample(frac=1)
 import string
 data['patterns']=data['patterns'].apply(lambda wrd: ''.join(wrd))
 data['patterns'] = data['patterns'].apply(lambda wrd: [ltrs.lower() for ltrs in wrd if ltrs not in string.punctuation])

 from tensorflow.keras.preprocessing.text import Tokenizer
 from tensorflow.keras.preprocessing.sequence import pad_sequences

 from sklearn.preprocessing import LabelEncoder


 tokenizer = Tokenizer(num_words=2000)
 tokenizer.fit_on_texts(data['patterns'])
 train = tokenizer.texts_to_sequences(data['patterns'])
 X_train = pad_sequences(train)

 le = LabelEncoder()
 y_train = le.fit_transform(data['tags'])
 from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Flatten
 from tensorflow.keras.models import Model
 input_shape=X_train.shape[1]

 vocabulary=len(tokenizer.word_index)

 output_length=le.classes_.shape[0]
 i = Input(shape=(input_shape,))
 x = Embedding(vocabulary + 1, 10)(i)
 x = Flatten()(x)
 x = Dense(output_length, activation='softmax')(x)

 import random
 import string
 import numpy as np
 import random
 import string
 
  
 pi=name
 texts_p = pd.Series([pi])
 texts_p = texts_p.apply(lambda wrd: ''.join(wrd))
 texts_p = texts_p.apply(lambda wrd: [ltrs.lower() for ltrs in wrd if ltrs not in string.punctuation])




 pi=tokenizer.texts_to_sequences(texts_p)
 print(pi)
 pi=np.array(pi).reshape(-1)
 print(pi)
 pi=pad_sequences([pi],input_shape)
 print(pi)

 o=model.predict(pi)
 o=o.argmax()
 print(o)
 r=le.inverse_transform([o])[0]
 print("Going Mery:",random.choice(responses[r]))
 return random.choice(responses[r])
