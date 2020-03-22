import os
import sys
import csv
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

input_file=sys.argv[1]
output_file=sys.argv[2]

path=os.getcwd()
files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and i.startswith(input_file) and i.endswith('.csv')]


data=[]
data_relations=[]

for file in files:
	temp_data=[]
	with open(file) as csv_file:
		csv_data=csv.reader(csv_file)
		for row in csv_data:
			temp_data.append(row)
	data_relations.append(temp_data[0])
	data.append(temp_data[1:])



new_data=data


for k in range(len(data)):
	curr_prob=''
	for i in range(len(data[k])):
		if data[k][i][0]!='':
			data[k][i][0]=data[k][i][0].replace('\n','')
			curr_prob=data[k][i][0]
		else:
			data[k][i][0]=curr_prob
		for j in range(len(data[k][i])):
			data[k][i][j]=data[k][i][j].replace('\n','')
			arr=data[k][i][j].split()
			new_data[k][i][j]=' '.join(l + '\n' * (n % 4 == 3) for n, l in enumerate(arr))


new_data=[np.asarray(arr) for arr in new_data]
source_entities=[]
relations=[]
target_entities=[]

for k in range(len(new_data)):

	distinct_probs=list(set(new_data[k][:,0]))

	source_entities.extend(['troubleshooting']*len(distinct_probs))
	relations.extend([data_relations[k][0]]*len(distinct_probs))
	target_entities.extend(distinct_probs)


	source_entities.extend(new_data[k][:,0])
	relations.extend([data_relations[k][1]]*new_data[k].shape[0])
	target_entities.extend(new_data[k][:,1])


	source_entities.extend(new_data[k][:,1])
	relations.extend([data_relations[k][2]]*new_data[k].shape[0])
	target_entities.extend(new_data[k][:,2])



kg_df = pd.DataFrame({'source':source_entities, 'target':target_entities, 'edge':relations})

G=nx.from_pandas_edgelist(kg_df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())

plt.figure(figsize=(40,40))
pos = nx.spring_layout(G)
d={(source_entities[i],target_entities[i]):relations[i] for i in range(len(relations))}
nx.draw(G, with_labels=True, node_color='skyblue', node_size=8000, node_shape='s' ,pos=pos,font_size=6)
nx.draw_networkx_edge_labels(G,pos,edge_labels=d,font_size=6)
plt.savefig(output_file)