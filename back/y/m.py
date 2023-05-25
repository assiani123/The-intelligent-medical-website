def c():
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
  model = Model(i, x)
  model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=['accuracy'])
  train=model.fit(X_train,y_train,epochs=200)
  return model
