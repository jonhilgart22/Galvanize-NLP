__author__ = 'Jonathan Hilgart'
#encoding utf-8
from textblob import TextBlob
from collections import Counter
from collections import defaultdict
import numpy as np

def prob_distribution(counter):
    """Return the probability based upon a counter dictionary"""
    return {k:value/sum(counter.values()) for k,value in counter.items()}


def cond_prob_bigram(end_word, first_word,prob_dist_bigram,prob_dist_unigram):
    """Conditional probability of word, given previous word. Predicting end word"""
    #Inspiration from http://norvig.com/spell-correct.html
    bigram = (first_word , end_word)
    try: # might not have the keys for a bigram
        if prob_dist_bigram[bigram] > 0 and prob_dist_unigram[first_word] > 0:

            return prob_dist_bigram[bigram] / prob_dist_unigram[first_word]
    except:
    # Average the back-off value and zero. This is the smoothing
        return prob_dist_unigram[end_word] / 2

def cond_prob_trigram(start,middle,end,prob_dist_trigram,prob_dist_bigram,prob_dist_unigram):
    """Find the conditional probability of a trigram model given the two previous words. Predicting the end word."""
    #Inspiration from http://norvig.com/spell-correct.html
    trigram = (start ,middle , end)
    bigram = ( start,middle)
    try: ## might not have the keys for a trigram
        if prob_dist_trigram[trigram] > 0 and prob_dist_bigram[bigram] > 0 and prob_dist_unigram[start] >0:

            return prob_dist_trigram[trigram] / prob_dist_bigram[bigram] ##return prob of trigram over first two words
    except:
        try: #might not find a bigram
            if prob_dist_bigram[bigram] > 0 and prob_dist_unigram[start] >0: # Back off to bigram model
                return prob_dist_bigram[bigram] / prob_dist_unigram[start]
        except: # back off to unigram
             #back off to unigram model (three words). This is the smoothing
            return prob_dist_unigram[end] / 3
        
def sentence_generate(probability_dict_unigram, probability_dict_bigram,probability_dict_trigram,number_of_sentences,prob_dist_trigram,prob_dist_bigram,prob_dist_unigram,text_counter_bigram,text_counter_trigram):
    """Generate random sentences based upon the probabilities given the the probability_dict"""
    number=0
    generated_text=[]
    character_counter = 0   
    #Find starting word of sentences using unigram proab
    sentence_endings = ["?","!","."]
    starting_chars = [item[1]  for item in list(probability_dict_bigram.keys()) if item[0] in sentence_endings]
    starting_chars_counter = Counter(starting_chars)
    #find list of unigram probabilities for starting characters
    starting_prob = prob_distribution(starting_chars_counter)
    #Pick an initial starting character
    start_char_index = np.random.choice([i for i in range(len(starting_prob.keys()))],1,p=list(starting_prob.values()))
    generated_text.append(starting_chars[start_char_index])
    while number !=number_of_sentences: #make sure we have this number of sentences. Keep generating sentences if not.
        if len(generated_text)<3:
            words_list = list(probability_dict_bigram.keys())
            prev_character=generated_text[character_counter]
            current_word_options = [i[1] for i in text_counter_bigram if i[0]==prev_character] #Find bigrams with prev char
            prob_bigram_list = []
            for curr_word in current_word_options:
                prob_bigram_list.append(cond_prob_bigram(curr_word,prev_character,prob_dist_bigram,prob_dist_unigram))
            # weighted choice algorithm
            # http://stackoverflow.com/questions/22722079/choosing-elements-from-python-list-based-on-probability
            # 1) pick random number between 0 and 1
            # 2) walk through the list, subtracting each item from your number as your go
            # 3 ) when you go to 0 or below, pick the current item
            weight = np.random.random()
            bigram_word_index = 0
            for index,prob in enumerate(prob_bigram_list):
                weight -=prob
                if weight <0:
                    bigram_word_index=index
            word = current_word_options[bigram_word_index]
            generated_text.append(word)
            character_counter+=1 ## go to the next character
        elif len(generated_text)>2: ###trigram 
            words_list = list(probability_dict_trigram.keys()) ## list of all trigram
            first_character=generated_text[character_counter] # find the previous word (one index away)
            second_character=generated_text[character_counter-1] #find the previous word to the previous word
            current_triword_options= []
            prob_trigram_list = [] #list of conditional probabilities associated with the last word in the trigram
            for i in text_counter_trigram:
                if i[1]==first_character and i[0]==second_character: ##the first two words of our trigram
                    curr_word = i[2] #the current word to predict
                    prob_trigram_list.append(cond_prob_trigram(second_character,first_character,curr_word,prob_dist_trigram,prob_dist_bigram,prob_dist_unigram)) ##add prob
                    current_triword_options.append(curr_word) ##add the possible word to our list
            if len(current_triword_options)==0: ## we do not have any options to continue the sentence.
                break
            weight = np.random.randint(1,sum(prob_trigram_list)*100000000)##need to change the weight because the triword options don't sum to 100%
            weight = weight/100000000# back to probabilities
            for index,prob in enumerate(prob_trigram_list):
                weight -=prob
                if weight <0: ## pick this as the word to add to the sentence
                    word = current_triword_options[index]
                    break
            generated_text.append(word)
            character_counter+=1 ## go to the next character 
        if word in (".","!","?"): ##end of the sentence
            number+=1
    first_word = generated_text[0][0].upper()+generated_text[0][1:]
    sentence = first_word+' '
    for index,word in enumerate(generated_text[1:]):
        if generated_text[index] in (".","!","?"):
            sentence +=word[0].upper()+word[1:]+' '
        else:
            sentence +=word +' '
    return sentence

