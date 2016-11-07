# Lab Feedback

## Week1-1: Welcome and NLP Overview
Looks Good
## Week1-2: Text Processing & Regular Expressions I
Looks Good
## Week1-3: Regular Expressions II
SpamLord:
Glad to see you're writing your own test cases

```python
#make one email regex by joining all the other patterns
emailregex = "|".join([test_patternemail_1,test_patternemail_2,test_patternemail_3])

for line in f:
    matches = re.findall(emailregex,line)
    matches_phone = re.findall(test_patternphone_1, line)

  #now you only need one for loop
  for match in matches:
       print(match,'match --- longform 8')
       email= '{}@{}'.format(*match)
       results.append((name,'e',email))

  for match in matches_phone:
      print(match,'match  phone-------')
      if match[0][0]=="(":
          area_code = match[0][1:4]
      else:
          area_code = match[0]

      try:
          phone= '{}-{}-{}'.format(area_code,match[1],match[2])
          results.append((name,'p',phone))
      except:
          print('failed')

```
## Week1-4: Segmenting, Tokenizing, & Stemming
Looks Good
## Week2-1: Text Encoding
Looks Good
## Week2-2: Edit Distance
```python
if c1==c2:
    # substitutions =previous_row[j]+0
    # there is no need to add a 0
    substitutions = previous_row[j]
else:

    substitutions =previous_row[j]+1 # TODO: WRITE CODE TO DETEMINE SUBSTITUTION
```

## Week2-3: Language Modeling I
TODO: Why does the probability of this phrase go down with bigram word?

The probability goes down because "the the" does not appear often in the corpus. Thus the model interprets this as a low probability of seeing "the the"


TODO: Why does the probability of this phrase go way up with bigram word?

the bigrams "Of the" and "the same" are seen a lot in our corpus, thus they have a high probability of occurring. However, the product of the unigrams "of", "the" and "same" are lower because one of those words isn't seen a lot in our corpus. 
## Week2-4: Language Modeling II

## Week3-1: Spelling Correction

## Week3-2: Word Tagging

## Week3-3: Named Entity Recognition (NER)

## Week3-4: Chatbots I

## Week4-1: Chatbots II

## Week4-2: Review/Project Check In

## Week4-3: Information Retrieval I

## Week4-4: Information Retrieval II

## Week5-1: Information Retrieval Project

## Week5-2: Naive Bayes

## Week6-1: Sentiment Analysis

## Week6-2: Non-negative Matrix Factorization (NMF)

## Week6-3: Latent Dirichlet Allocation (LDA)

## Week6-4: Topic Modeling Project

## Week7-1: Word2Vec

## Week7-2: Doc2Vec

## Week7-3: Everything2Vec

## Week7-4: Future of NLP Guest Lecture

## Week8: Final Presentation:
