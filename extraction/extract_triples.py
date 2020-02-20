from openie import StanfordOpenIE
import csv
import sys
import pickle


f=open(sys.argv[1],'rb')
sentences=pickle.load(f)
f.close()
print(len(sentences))

f=open(sys.argv[2],'w+')
writer=csv.writer(f)

writer.writerow(['SENTENCE','TRIPLES'])

with StanfordOpenIE() as client:
	for i in range(len(sentences)):
		sentence=sentences[i]
		triples=''
		for triple in client.annotate(sentence):
			triples+='|-  '+ str(triple)+'\n'
		writer.writerow([sentence,triples])
		if i%10==0:
			print(i)


f.close()

