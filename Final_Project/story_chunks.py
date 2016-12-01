__author__='Jonathan Hilgart'
# utility_items='Pocketknife Flashlight'.split(' ')
# funny_items='Half-eaten-sandwich broken-lightbulb'.split(' ')
# transportation_items = 'Skateboard Bike Rollerblades'.split(' ')


def place_of_story(story_section,protag,antag,pl_one,lang_one,trump_speech,pl_two=None):
	"""Story chunks to use for IR with cosine similarity. PL_one is place_one variable, pl_two is place two variable. 
	protag and antag are protagonist and antagonist defined in the story."""
	if story_section==1:
		return ['You have the feeling that something bad was going to happen so you pull out your pocketknife. {} looks at you and asks,"So what do you\
		think you are going to do with that? That is not going to save you. You notice {} in the distance and you yell to trump "Run for it!"'\
		.format(protag,pl_one),
		'All of a sudden, you remember that you have not eaten lunch. "Silly me!" you think to yourself as your pull out your half-eaten-sandwich.\
		You chew happily for a while before deciding it was time to more on. "Time to go you mention to Trump". As you walk you suddenly come across {} \
		who asks "What are ye doing here?" '.format(antag),

		' After talking with {} you asked "What do we do around here?". {} replies, "Currently, I am avoiding {} because they are looking\
		to round up everyone who speaks {}!" "Oh no!" You think to yourself "They are going to capture Trump!"Trump turns and says {} \
		"Wow, he really has a way with words," you think. Would should you do next?'.format(protag,protag,antag,lang_one,trump_speech)  # protag, protag , antag, language , trump

		]
	else:
		pass
