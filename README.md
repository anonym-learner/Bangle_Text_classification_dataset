# Bangla-Text-Classification-Dataset

We have curated a comprehensively large dataset of 2,58,960 Bangla documents labeled with eight different categories that was used for development and testing purpose in some of our thesis works. These articles have been collected with a web crawler from several online Bangla news portals, blogs and magazines. This corpus is open sourced for public usage and we expect that this dataset will help the natural language research community to reinforce NLP tasks in Bangla
## Corpus-Description

Total Documents: 2,58,960

Total Categories: 8

 Categories:  
-জাতীয় (State)    
-আন্তর্জাতিক (International)  
-অর্থনীতি (Economy)   
-খেলাধুলা (Sports)   
-বিজ্ঞান ও প্রযুক্তি (Science and Technology)   
-বিনোদন (Entertainment)  
-স্বাস্থ্য ও জীবনবিধি (Health and Lifestyle)   
-শিল্প ও সাহিত্য (Arts and Literature)   

Number of Documents per Category:  
-জাতীয়: 75,974  
-আন্তর্জাতিক: 33,776  
-অর্থনীতি: 20,922  
-খেলাধুলা: 53,901  
-বিজ্ঞান ও প্রযুক্তি: 11,004  
-বিনোদন: 34,702  
-স্বাস্থ্য ও জীবনবিধি: 13,467  
-শিল্প ও সাহিত্য: 15,214    

## Drive Link
https://drive.google.com/file/d/1sOew2kfLeAi8BsmGhWmOXj0RpOgbLLm-/view?usp=sharing

## preprocess_text.py
punctuation marks, digits and special characters are removed. Then each document is tokenized using blank space which results in a list of words. Then stop words are excluded from that list. We have collected 430 Bangla stopwords (stop.txt) that hold no importance in classifying the documents rather increase haziness during the learning session of the models.
