The various files that are executable:
1. main.py - implements the vanilla VSM model
2. main_ESA - implements Explicit Semantic Analysis
3. main_LSA_skl - implements Latent Semantic Analysis using BOW and TFIDF
4. main_W2v - implements pretrained Word2Vec with LSA
5. main_newW2V - implements word2vec trained from scratch with LSA


To test your code, run main.py (or its different versions according to the model you want to run) as before with the appropriate arguments.
Usage: main.py [-custom] [-dataset DATASET FOLDER] [-out_folder OUTPUT FOLDER]
               [-segmenter SEGMENTER TYPE (naive|punkt)] [-tokenizer TOKENIZER TYPE (naive|ptb)] 

When the -custom flag is passed, the system will take a query from the user as input. For example:
> python main.py -custom
> Enter query below
> Papers on Aerodynamics
This will print the IDs of the five most relevant documents to the query to standard output.

When the flag is not passed, all the queries in the Cranfield dataset are considered and precision@k, recall@k, f-score@k, nDCG@k and the Mean Average Precision are computed.

In both the cases, *queries.txt files and *docs.txt files will be generated in the OUTPUT FOLDER after each stage of preprocessing of the documents and queries.