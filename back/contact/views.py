




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


from rest_framework.parsers import JSONParser
from contact.models import E, messg, rdv,messgm

from django.http.response import JsonResponse
from rest_framework.decorators import api_view


from rest_framework import serializers
from contact.models import  E,User,notm,notp

def index ():
  return 1 
from datetime import datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token 
from .serializers import U, ms, rdvs,msm,notps,notms
from y.s import po
from y.m import c
import tensorflow as tf
import pandas as pd
import random
import json
with open('y/m.json') as json_data:

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
model2 = Model(i, x)
model2.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=['accuracy'])
train=model2.fit(X_train,y_train,epochs=200)










'''@api_view(['GET'])
def dapi(request):
    b = Book.objects.all()
    s = BS(b, many=True)
    return Response(s.data)
@api_view(['POST'])
def papi(request):
    d=request.data
    s=DSerializer(data=d)
    if s.is_valid():
        s.save()
        return Response(s.data)
@api_view(['GET'])
def yas(request, pk):
    b = Book.objects.get(pk=pk)
    s = BS(b)
    return Response(s.data)
@api_view(['PUT'])
def y(request, pk):
    b = Book.objects.get(pk=pk)
    s=BS(b,data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data)
@api_view(['DELETE'])
def ass(request, pk):
    b = Book.objects.get(pk=pk)
    b.delete()
    return Response([1,2])
@api_view(['GET', 'PUT', 'DELETE'])
def com(request, pk):
    b = Book.objects.get(pk=pk)
    if request.method == 'GET':
        s = BS(b)
        return Response(s.data)
    elif request.method=='PUT':
        s=BS(b,data=request.data)
        if s.is_valid():
         s.save()
         return Response(s.data)
    elif request.method=='DELETE':
        b.delete()
        return Response([1,2])'''



from rest_framework import status

@api_view(['POST'])
def reg(request):
    d = request.data
    s = U(data=d)
    if s.is_valid():
        s.save()
        return Response(s.data, status=status.HTTP_201_CREATED)
    else:
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def log(request):
    email = request.data.get('email')
    password = request.data.get('password')


    try:
        user = User.objects.get(email=email ,role="p")
        uu=U(user)
        
    except User.DoesNotExist:
        
      return Response(['ne'])

    if not user.check_password(password):
        
       return Response(['nc'])
    # Authentification réussie
    # Générez un token JWT ou utilisez la session pour gérer l'authentification à partir de ce point.

    return Response([uu.data])
@api_view(['POST'])
def logm(request):
    email = request.data.get('email')
    password = request.data.get('password')


    try:
        user = User.objects.get(email=email ,role="m")
        uu=U(user)
        
    except User.DoesNotExist:
        
      return Response(['ne'])

    if not user.check_password(password):
        
       return Response(['nc'])
    # Authentification réussie
    # Générez un token JWT ou utilisez la session pour gérer l'authentification à partir de ce point.

    return Response([uu.data])
@api_view(['POST'])
def prdv(request):
    d = request.data
    s = rdvs(data=d)
    if s.is_valid():
        s.save()
        return Response(s.data)
    else:
        return Response(s.errors, status=400)
@api_view(['POST'])
def g(request):
    spec = request.data.get('spec')
    
    users = User.objects.filter(spec=spec)
    uu = U(users, many=True)
    
    return Response(uu.data)
@api_view(['GET'])
def rd(request, nom):
    u = rdv.objects.filter(nomp=nom)
    s = rdvs(u,many=True)
    return Response(s.data)
@api_view(['DELETE'])
def jj(request, pk):
    b = rdv.objects.get(pk=pk)
    b.delete()
    return Response([1,2])
@api_view(['GET'])
def rdm(request, nom):
    u = rdv.objects.filter(nomm=nom)
    s = rdvs(u,many=True)
    return Response(s.data)
@api_view(['PUT'])
def up(request, pk):
    b = rdv.objects.get(pk=pk)
    s = rdvs(b, data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data)
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def m(request):
    e=request.data


    nome = "cp"
    nomc = e["nome"]
    mesg = e["mesg"]
    if(po(mesg,model))=="k":
     c = datetime.now()
   
     f = "lwa9et w date tw ye si chbeb est "+c.strftime("%Y-%m-%d %H:%M:%S")
     
     data = {
        'nome': nome,
        'nomc': nomc,
        'mesg': f

     }
    if (po(mesg,model)=="e"):
          f="nty Mr "+nomc +" bkolou charftna ye 8ali"
          data = {
        'nome': nome,
        'nomc': nomc,
        'mesg': f
          }
    if(po(mesg,model)!="e" and po(mesg,model)!="k") :
         data = {
        'nome': nome,
        'nomc': nomc,
        'mesg': po(mesg,model)

     }
    
    
        
    s = ms(data=e)
    serializer = ms(data=data)
    if serializer.is_valid() and s.is_valid():
        s.save()
        serializer.save()
        return Response([serializer.data,s.data])
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def message(request, n):
    u = messg.objects.filter(nome=n) | messg.objects.filter(nomc=n)
    s = ms(u, many=True)
    return Response(s.data)
@api_view(['GET'])
def messagem(request, n):
    u = messgm.objects.filter(nome=n) | messgm.objects.filter(nomc=n)
    s = msm(u, many=True)
    return Response(s.data)


@api_view(['POST'])
def mm(request):
    e=request.data


    nome = "cm"
    nomc = e["nome"]
    mesg = e["mesg"]

    data = {
        'nome': nome,
        'nomc': nomc,
        'mesg': po(mesg,model2)

    }
    
    
        
    s = msm(data=e)
    serializer = msm(data=data)
    if serializer.is_valid() and s.is_valid():
        s.save()
        serializer.save()
        return Response([serializer.data,s.data])
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def em(request, pk):
    b = User.objects.get(pk=pk)
    s = U(b)
    return Response(s.data)
@api_view(['PUT'])
def pem(request, pk):
    user = User.objects.get(pk=pk)
    serializer = U(user, data=request.data, partial=True)  # Use partial=True to allow partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def nop(request):
    d = request.data
    s = notps(data=d)
    if s.is_valid():
        s.save()
        return Response(s.data)
    else:
        return Response(s.errors, status=400)
@api_view(['POST'])
def nom(request):
    d = request.data
    s = notms(data=d)
    if s.is_valid():
        s.save()
        return Response(s.data)
    else:
        return Response(s.errors, status=400)
@api_view(['GET'])
def gnm(request, n):
    u = notm.objects.filter(nomm=n) 
    s =notms(u, many=True)
    return Response(s.data)
@api_view(['GET'])
def gnp(request, n):
    u = notp.objects.filter(nomp=n) 
    s =notps(u, many=True)
    return Response(s.data)



    