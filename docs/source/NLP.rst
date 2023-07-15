NLP
====


NLP dataset
-------------

IMDb Reviews: http://ai.stanford.edu/~amaas/data/sentiment/

.. code-block:: console 

    E:\Dataset\NLPdataset> wget  http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz -o aclImdb_v1.tar.gz
    E:\Dataset\NLPdataset> tar -xf .\aclImdb_v1.tar.gz
    E:\Dataset\NLPdataset> ls .\aclImdb\

    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----         4/12/2011  10:22 AM                test
    d-----         6/25/2011   6:09 PM                train
    -a----         4/12/2011  10:14 AM         845980 imdb.vocab
    -a----         6/11/2011   3:54 PM         903029 imdbEr.txt
    -a----         6/25/2011   5:18 PM           4037 README

    E:\Dataset\NLPdataset> ls .\aclImdb\train\

    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----         4/12/2011   2:47 AM                neg
    d-----         4/12/2011   2:47 AM                pos
    d-----         4/12/2011   2:47 AM                unsup
    -a----         4/12/2011  10:17 AM       21021197 labeledBow.feat
    -a----         4/12/2011  10:22 AM       41348699 unsupBow.feat
    -a----         4/12/2011   2:48 AM         612500 urls_neg.txt
    -a----         4/12/2011   2:48 AM         612500 urls_pos.txt
    -a----         4/12/2011   2:47 AM        2450000 urls_unsup.txt

Sentiment Analysis tutorials:
https://huggingface.co/blog/sentiment-analysis-python


SQuAD dataset
-------------
The dataset that is used the most as an academic benchmark for extractive question answering is SQuAD. There is also a harder SQuAD v2 benchmark, which includes questions that don't have an answer. Your own dataset should contain a column for contexts, a column for questions, and a column for answers.

SQuAD: https://rajpurkar.github.io/SQuAD-explorer/
https://rajpurkar.github.io/SQuAD-explorer/explore/v2.0/dev/

.. code-block:: console 

    E:\Dataset\NLPdataset\squad> wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json -O train-v2.0.json

QA tutorials:
https://huggingface.co/docs/transformers/tasks/question_answering
https://huggingface.co/learn/nlp-course/chapter7/7?fw=pt
https://huggingface.co/transformers/v4.1.1/custom_datasets.html#question-answering-with-squad-2-0
A Model for Open Domain Long Form Question Answering: https://yjernite.github.io/lfqa.html

Reference
----------

https://umap-learn.readthedocs.io/en/latest/index.html

Natural Language Processing with Transformers Book
https://github.com/nlp-with-transformers/notebooks

CS224N: Natural Language Processing with Deep Learning
https://web.stanford.edu/class/cs224n/

DistilBERT, a Distilled Version of BERT: Smaller, Faster, Cheaper and Lighter", (2019)

CARER: Contextualized Affect Representations for Emotion Recognition
Unlike most sentiment analysis datasets that involve just "positive" and "negative" polarities, this dataset contains six basic emotions: anger, disgust, fear, joy, sadness, and surprise. Given a tweet, our task will be to train a model that can classify it into one of these emotions.