import sys
import pickle

f=open(sys.argv[1],'r')
text=f.read().replace('\n',' ').replace('\x0c','')
f.close()

sentences=text.split('.')
sentences=[sent.lstrip() for sent in sentences]
sentences=[sent+'.' for sent in sentences]

f=open(sys.argv[2],'wb')
pickle.dump(sentences,f)
f.close()

f=open(sys.argv[2],'rb')
print(pickle.load(f))
f.close()