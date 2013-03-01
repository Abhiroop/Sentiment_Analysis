from __future__ import division
from nltk import PorterStemmer
def func(feed):
	pos_sent=open("positive.txt").read()
	neg_sent=open("negative.txt").read()
	positive_counter=0
	negative_counter=0
	neutral_counter=0
	feed_counter=0
	positive_weight=0
	negative_weight=0
	neutral_weight=0
	# burger=open('/home/miserysignals/burger.txt','r')
	#feed=burger.read()
	#feed=raw_input('Enter your feedback: ')
	positive_words=pos_sent.split('\n')
	negative_words=neg_sent.split('\n')
	neutral_words=['ordinary','average','neutral','allright','ok','soso']
	emotional_words=positive_words+negative_words+neutral_words

	# Convert to lower case
	feed_processed=feed.lower()

	# Remove Punctuation
	from string import punctuation
	for p in list(punctuation): 
		feed_processed=feed_processed.replace(p,'')

	# Find the words
	words=feed_processed.split(' ')

	for i in range(len(words)):
		#x=PorterStemmer().stem_word(words[i])	
		#y=PorterStemmer().stem_word(words[i-1])
		if words[i] in emotional_words:
			feed_counter=feed_counter+1
		if words[i] in positive_words:
			if words[i-1]=='not':
				negative_counter=negative_counter+1
			elif words[i-1]=='nothing' or words[i-1]=='been':
				neutral_counter=neutral_counter+1
			else:
				positive_counter=positive_counter+1
		elif words[i] in negative_words:
			if words[i-1]=='not':		
				neutral_counter=neutral_counter+1
			else:
				negative_counter=negative_counter+1
		elif words[i] in neutral_words:
				neutral_counter=neutral_counter+1
	try:	
		positive_weight=(positive_counter/feed_counter)
		negative_weight=(negative_counter/feed_counter)
		neutral_weight=(neutral_counter/feed_counter)
		weighted_mean=((positive_weight)*1)+((neutral_weight)*0)+((negative_weight)*(-1))
		return weighted_mean
	except ZeroDivisionError: pass



# Taking the feed
tot=[]
line=''
f=open('text.txt','r')
for c in f.read():
	if c == '\n':
		tot.append(line)
		line=''
	else:
		line=line+c
hal1=[]
hal2=[]
flag=[]
for i in tot:
	food=''
	feed=''
	r=''
	x=i.find(':')
	food,feed=i[:x],i[x+1:]
	hal1.append(food)
	flag.append(0)	
	frac=func(feed)
	hal2.append(frac)
print hal2
dist_food=[]
dist_count=[]
for trav in range(len(hal1)):
	if flag[trav] == 0:
		c=0.0
		for q in range(len(hal1)):
			if hal1[trav]==hal1[q]:
				c=c+hal2[q]
				flag[q]=1
		dist_food.append(hal1[trav])
		dist_count.append(c)
print dist_food
print dist_count
with open('output.txt','w') as myfile:
	for i in range(len(dist_food)):
		s=''
		s=dist_food[i]+' '+str(dist_count[i])+'\n'		
		myfile.write(s)
