# library
import pandas as pd 
import sys

# read in the file. 
x=pd.ExcelFile(sys.argv[1], encoding='utf-8', index_col=0)
df=x.parse('Sheet1')

# select columns 
df_select=df[['Word','Western Xiangxi', 'Eastern Xiangxi', 'Qiandong', 'Chuanqiandian', 'Diandongbei', 'Hmong Daw', 'Hmong Njua', 'Bunu', 'Baonao', 'Numao', 'Longhua Jiongnai', 'Liuxiang Jiongnai', 'Xiaozhai Younuo', 'Huangluo Younuo', 'Northern Pa-Hng', 'Southern Pa-Hng', 'Hm-Nai']]
# transpose the columns to rows
df_select_transpose=df_select.transpose()

word_list=[]
# create word list document
for i in df_select_transpose:
	temp=df_select_transpose[i].tolist()
	location=list(df_select_transpose.index)[1:]
	meaning=temp[0]	
	ipa_list=temp[1:]
	for j, val in enumerate(ipa_list):
		word_list.append({'Index':i+1,'CONCEPT':meaning,'LANGUAGE':location[j], 'IPA':ipa_list[j]})

#get ready for outputing
word_list_dataframe=pd.DataFrame(word_list)
word_list_dataframe=word_list_dataframe.set_index('Index')
word_list_dataframe=word_list_dataframe[['CONCEPT','LANGUAGE','IPA']]
word_list_dataframe.to_csv(sys.argv[2],encoding='utf-8',sep='\t')
# The encoding have to be utf-8 or it won't work in Lingpy (my experience)

	

