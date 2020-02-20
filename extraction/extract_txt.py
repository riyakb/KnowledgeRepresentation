import sys
import textract

text = textract.process(sys.argv[1],encoding='ascii')

f=open(sys.argv[2],'w+')
f.write(text.decode('ascii'))
f.close()