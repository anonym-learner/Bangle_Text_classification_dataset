import re

def preprocess_data(article_count, stop_words_filename,output_filename):
    fout = open(output_filename,'w', encoding="utf-8")
    fin1= open(stop_words_filename,'r', encoding="utf-8")
    st_words = fin1.readlines()
    fin1.close()
    stop_words={}
    for sw in st_words:
            stop_words[sw.strip()]=""
    for i in range(article_count):
        try:
                fin = open(str(i+1)+'.txt','r', encoding="utf-8")
        except FileNotFoundError:
                continue
        compl=fin.read()
        compl=compl.replace("\n","")
        compl=re.sub(r'[\\/“”0-9@&$%+_=<>~*#০১২৩৪৫৬৭৮৯(){}\[\]]+','',compl)
        #compl=re.sub(r'[0-9]+',"",compl)
        sentences = re.split('[–—\s.,\-\‘\’\‘\'\\\"।!?:;|]',compl)
        #sentences= compl.split("।")
        #for (String sentence : sentences) {
        #	String[] words=sentence.split("([.,*‘’() '\\\"]|\\s)+");
        #	for(String word:words)
        #		pw.print(word + " ");
        #	pw.println();
        #}
        label=""
        for x in sentences:
                if x not in stop_words and len(x)>=2:
                        label=label+" "+x
        label=label.replace("  "," ")
        fout.write(label+"\n")
        fin.close()
    fout.close()

