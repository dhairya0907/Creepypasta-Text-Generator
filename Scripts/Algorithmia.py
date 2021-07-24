import Algorithmia
from Algorithmia.errors import AlgorithmException
import numpy as np
import string
import keras
import re
import random
from tensorflow import keras
from numpy import load
from keras.layers import LSTM, Dense, Embedding, GRU


client = Algorithmia.client()

# Path to diffrent models and text files

charcter_level_lstm_model_small = ""
character_level_lstm_text_small = ""
character_level_lstm_sequences_small = ""
charcter_level_lstm_model_medium = ""
character_level_lstm_text_medium = ""
character_level_lstm_sequences_medium = ""
charcter_level_lstm_model_large = ""
character_level_lstm_text_large = ""
character_level_lstm_sequences_large = ""

charcter_level_gru_model_small = ""
character_level_gru_text_small = ""
character_level_gru_sequences_small = ""
charcter_level_gru_model_medium = ""
character_level_gru_text_medium = ""
character_level_gru_sequences_medium = ""
charcter_level_gru_model_large = ""
character_level_gru_text_large = ""
character_level_gru_sequences_large = ""

word_level_lstm_model_small = ""
word_level_lstm_model_medium = ""
word_level_lstm_model_large = ""
word_level_lstm_text_small_medium = ""
word_level_lstm_text_large = ""

word_level_gru_model_small = ""
word_level_gru_model_medium = ""
word_level_gru_model_large =""
word_level_gru_text_small_medium_large = ""


def pre_load_model(path):
    
    model_path = client.file(path).getFile().name
    model = keras.models.load_model(model_path)
    
    return model
        
def load_text(path):
    
    file_path = client.file(path).getFile().name
    file = open(file_path)
    file = file.read()
    
    return file
    

def charcter_level_lstm_sample(preds, temp):
    
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temp
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    
    return np.argmax(probas)
    


def charcter_level_predict(size,temp,length,start,mtype):
    
    if size == 1:
        if mtype == 'lstm':
            model = pre_load_model(charcter_level_lstm_model_small)
            text = load_text(character_level_lstm_text_small)
            sequences_path = client.file(character_level_lstm_sequences_small).getFile().name
            dict_data = load(sequences_path)
        else:
            model = pre_load_model(charcter_level_gru_model_small)
            text = load_text(character_level_gru_text_small)
            sequences_path = client.file(character_level_gru_sequences_small).getFile().name
            dict_data = load(sequences_path)
    
    if size == 2:
        if mtype == 'lstm':
            model = pre_load_model(charcter_level_lstm_model_medium)
            text = load_text(character_level_lstm_text_medium)
            sequences_path = client.file(character_level_lstm_sequences_medium).getFile().name
            dict_data = load(sequences_path)
        else:
            model = pre_load_model(charcter_level_gru_model_medium)
            text = load_text(character_level_gru_text_medium)
            sequences_path = client.file(character_level_gru_sequences_medium).getFile().name
            dict_data = load(sequences_path)
        
    if size == 3:
        if mtype == 'lstm':
            model = pre_load_model(charcter_level_lstm_model_large)
            text = load_text(character_level_lstm_text_large)
            sequences_path = client.file(character_level_lstm_sequences_large).getFile().name
            dict_data = load(sequences_path)
        else:
            model = pre_load_model(charcter_level_gru_model_large)
            text = load_text(character_level_gru_text_large)
            sequences_path = client.file(character_level_gru_sequences_large).getFile().name
            dict_data = load(sequences_path)
    
    model.compile(optimizer=keras.optimizers.Adam(), loss = keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])
    
    characters = sorted(list(set(text)))
    n_to_char = {n:char for n, char in enumerate(characters)}
    char_to_n = {char:n for n, char in enumerate(characters)}
    vocab_size = len(characters)
    
    X = dict_data['arr_0']
    
    if start == "":
        start = np.random.randint(0, len(X)-1)
        string_mapped = list(X[start])
        full_string = [n_to_char[value] for value in string_mapped]
        
    else:
        string_mapped = list(start)
        string_mapped = [char_to_n[value] for value in string_mapped]
        full_string = [n_to_char[value] for value in string_mapped]
    
    for i in range(length):
        x = np.reshape(string_mapped, (1, len(string_mapped), 1))
        x = (x / float(len(characters))) + (np.random.rand(1, len(string_mapped), 1) * 0.01)
        prediction = model.predict(x, verbose=0)
        pred_index = charcter_level_lstm_sample(np.ndarray.flatten(prediction),temp)
        seq = [n_to_char[value] for value in string_mapped]
        full_string.append(n_to_char[pred_index])
        string_mapped.append(pred_index)
        string_mapped = string_mapped[1:len(string_mapped)]
        
    txt=""
    for char in full_string:
        txt = txt+char
        
    return txt
    

vocab = ""
vocab_len_highest = ""
text = ""
vocab = ""
index_to_word = ""
word_to_index = ""
file_string = ""
model_new = ""



def normalize(s):
    chars = string.punctuation
    for c in chars:
        s = s.replace(c," "+c+" ")
    s = s.lower()
    
    return s
    
def accept(words):
    for word in words:
        if(not word in vocab):
            return False
            
    return True
    
def text_to_index(s):
    s = normalize(s)
    s_words = s.split()
    if (not accept(s_words)):
        return ""
        
    return np.array([word_to_index[word] for word in s_words])
    
def word_list_to_index(s_words):
    if (not accept(s_words)):
        return ""
        
    return np.array([word_to_index[word] for word in s_words])
    
def index_to_text(inds):
    s = ""
    for i in range(inds.shape[0]):
        s += index_to_word[inds[i]] + " "
        
    return s
    
    
def predictRandom(s, numWords, conf):
    
  s_return = s
  s_ind = text_to_index(s)
  
  model_new.reset_states()
  
  for i in range(s_ind.shape[0]):
    pred = model_new.predict_on_batch(np.array(s_ind[i]).reshape(1,1))
    
  for i in range(numWords):
    pred_new = np.power(pred[0], conf)
    pred_new = pred_new / np.sum(pred_new)
    
    next_word_ind = np.random.choice(np.arange(vocab_len_highest), p = pred_new)
    
    s_return += " " + index_to_word[next_word_ind]
    pred = model_new.predict_on_batch(np.array(next_word_ind).reshape(1,1))
  
  return s_return

def get_random_str(main_str, substr_len):
    start = ""
    main_str = main_str.split()
    idx = random.randrange(0, len(main_str) - substr_len + 1)
    for i in range(idx,(idx+substr_len)):
        if i == 0:
            start = main_str[i]
        else:
            start = start + " " + main_str[i]
    return start


def word_level_predict(size,temp,length,start,mtype):
    
    global vocab
    global vocab_len_highest
    global text
    global index_to_word
    global word_to_index
    global file_string
    global model_new
    
    file_string = "believed , ? mosquitoes"
    
    if start == "":
        text = load_text(word_level_lstm_text_small_medium)
        start = get_random_str(text, 20)
    
    if size == 1:
        if mtype == 'lstm':
            vocab_len_highest = 39753
            model = pre_load_model(word_level_lstm_model_small)
            text = load_text(word_level_lstm_text_small_medium)
            if (text.find(start) == -1):
                text = text + start
        else:
            vocab_len_highest = 39753
            model = pre_load_model(word_level_gru_model_small)
            text = load_text(word_level_gru_text_small_medium_large)
            if (text.find(start) == -1):
                text = text + start
            
    elif size == 2:
        if mtype == 'lstm':
            vocab_len_highest = 39753
            model = pre_load_model(word_level_lstm_model_medium)
            text = load_text(word_level_lstm_text_small_medium)
            if (text.find(start) == -1):
                text = text + start
        else:
            vocab_len_highest = 39753
            model = pre_load_model(word_level_gru_model_medium)
            text = load_text(word_level_gru_text_small_medium_large)
            if (text.find(start) == -1):
                text = text + start
            
    else :
        if mtype == 'lstm':
            vocab_len_highest = 30360
            model = pre_load_model(word_level_lstm_model_large)
            text = load_text(word_level_lstm_text_large)
            if (text.find(start) == -1):
                text = text + start
        else:
            vocab_len_highest = 39753
            model = pre_load_model(word_level_gru_model_large)
            text = load_text(word_level_gru_text_small_medium_large)
            if (text.find(start) == -1):
                text = text + start
            
    
    vocab = set(text.split())
    index_to_word = {i: word for i, word in enumerate(vocab)}
    word_to_index = {word: i for i, word in index_to_word.items()}
    
    model.compile(optimizer=keras.optimizers.Adam(), loss = keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])
   
    text_ind = word_list_to_index(text)
    
    if mtype == 'lstm':
        model_new = keras.Sequential()
        model_new.add(Embedding(vocab_len_highest, 30, batch_input_shape = (1, 1)))
        model_new.add(LSTM(64, return_sequences = True, stateful = True))
        model_new.add(LSTM(128, return_sequences = False, stateful = True))
        model_new.add(Dense(vocab_len_highest, activation = "softmax"))
        model_new.set_weights(model.get_weights())
        model_new.compile(optimizer=keras.optimizers.Adam(), loss = keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])
    else:
        model_new = keras.Sequential()
        model_new.add(Embedding(vocab_len_highest, 30, batch_input_shape = (1, 1)))
        model_new.add(GRU(64, return_sequences = True, stateful = True))
        model_new.add(GRU(128, return_sequences = False, stateful = True))
        model_new.add(Dense(vocab_len_highest, activation = "softmax"))
        model_new.set_weights(model.get_weights())
        model_new.compile(optimizer=keras.optimizers.Adam(), loss = keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])
    
    return predictRandom(start, length, temp)
    

def apply(input):
    
    if(input["level"] == "character level"):
        return charcter_level_predict(input["model"],input["temperature"],input["length"],input["starting"],input["type"])
    
    else:
        return word_level_predict(input["model"],input["temperature"],input["length"],input["starting"],input["type"])
    