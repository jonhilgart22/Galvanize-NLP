__author__='Jonathan Hilgart'

from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import re

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

		print('The acuracy is :{:.2%}'.format(number_correct/(number_correct+number_incorrect)))
		print('The query that failed was :',[list_of_lists_of_queries[i] for i in incorrect])
	else:
		print('The acuracy is :{:.2%}'.format(number_correct/(number_correct+number_incorrect)))
	#return "The accuracy is :{}".format(number_correct/(number_incorrect+number_incorrect))
