__author__='Jonathan Hilgart'

from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import re
import textblob
import gensim

def accuracy_score_test(list_of_lists_of_queries,story_chunk_responses,item_keyword):
	"""Calculate the accuracy of return the correct response from each story chunk given the keyword of the item the user input"""

	number_correct=0
	number_incorrect=0
	incorrect = []
	for idx,query in enumerate(list_of_lists_of_queries):
		tfidf= TfidfVectorizer()  #create a model
		tf_idf_story= tfidf.fit_transform(story_chunk_responses) ##tf-idf on the possible story chunks in storychunk_one
		query_tfidf = tfidf.transform(query) ## turn the user sentence into a vector
		cosine_sim = linear_kernel(tf_idf_story,query_tfidf).flatten() ## cosine similarity between the story chunks and user sentence
		section = re.sub(r'(\t)','',story_chunk_responses[cosine_sim.argsort()[::-1][0]] )
		if item_keyword in section:
			number_correct+=1
		else:
			number_incorrect+=1
			incorrect.append(idx)
	if number_incorrect !=0:

		return 'The acuracy is',float(number_correct/(number_correct+number_incorrect)),'The query that failed was :',[list_of_lists_of_queries[i] for i in incorrect]
	else:
		return 'The acuracy is',float(number_correct/(number_correct+number_incorrect))
	#return "The accuracy is :{}".format(number_correct/(number_incorrect+number_incorrect))


# See top related words from word2vec model
def word2vec(story_chunk,user_query):
	try:
	    one = ''
	    for i in story_chunk:
	        one+=i
	    blob_one= textblob.TextBlob(one)
	    sent_one = [i.tokens.lower() for i in blob_one.sentences]
	    one = one.lower()
	    membership = blob_one.tokens.lower()
	    query_words_one = user_query[0].lower().split(' ')
	    final_query_one=[]
	    count_one = 0
	    ### Check if the user input words are in our word2vec model, if not, we can not use them.
	    for input_one in query_words_one:
	        if input_one in membership:
	            final_query_one.append(input_one)
	    model_one = gensim.models.Word2Vec(sent_one, min_count=1)
	    print('The words most similar to the query words added together :',final_query_one)
	    return model_one.most_similar(positive=final_query_one)
	except:
		'There are no words in the story chunk that matches your input.'
