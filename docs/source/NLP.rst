NLP
====

Our Sample code
----------------

Sentiment 
~~~~~~~~~
Run nlp\huggingfaceclassifier2.py, based on args of "data_type=huggingface data_name=imdb model_checkpoint=bert-base-cased task=sentiment outputdir=./output traintag=0805 training=True total_epochs=4 save_every=2 batch_size=8 learningrate=2e-05"
The saved path is "outputpath=os.path.join(args.outputdir, task, args.data_name+'_'+args.traintag)"

.. code-block:: console 

    All keys in raw datasets: dict_keys(['train', 'test', 'unsupervised'])
    {'labels': torch.Size([8]), 'input_ids': torch.Size([8, 512]), 'token_type_ids': torch.Size([8, 512]), 'attention_mask': torch.Size([8, 512])}
    tensor(0.7184, grad_fn=<NllLossBackward0>) torch.Size([8, 2])

sequence_classifier
~~~~~~~~~~~~~~~~~~~~
Run nlp\huggingfaceclassifier2.py, based on args of "data_type=huggingface data_name=glue dataconfig=mrpc subset=0.1 model_checkpoint=bert-base-cased task=sequence_classifier outputdir=./output traintag=0807 training=True total_epochs=4 save_every=2 batch_size=8 learningrate=2e-05"

.. code-block:: console 

    oneitem all keys: dict_keys(['sentence1', 'sentence2', 'label', 'idx'])
    ClassLabel(names=['not_equivalent', 'equivalent'], id=None)
    {'labels': torch.Size([8]), 'input_ids': torch.Size([8, 80]), 'token_type_ids': torch.Size([8, 80]), 'attention_mask': torch.Size([8, 80])}
    tensor(0.7476, grad_fn=<NllLossBackward0>) torch.Size([8, 2])
    task sequence_classifier: {'accuracy': 0.8602941176470589, 'f1': 0.9028960817717206}

custom_classifier
~~~~~~~~~~~~~~~~~~

data_type=huggingface data_name=imdb dataconfig=None subset=0 model_checkpoint=bert-base-cased task=custom_classifier outputdir=./output traintag=0807 training=True total_epochs=4 save_every=2 batch_size=8 learningrate=2e-05
oneitem all keys: dict_keys(['text', 'label'])
{'labels': torch.Size([8]), 'input_ids': torch.Size([8, 512]), 'attention_mask': torch.Size([8, 512])}
['labels', 'input_ids', 'attention_mask']
tensor(0.6916, grad_fn=<NllLossBackward0>) torch.Size([8, 2])
task custom_classifier: {'accuracy': 0.93576}

token_classifier
~~~~~~~~~~~~~~~~~
data_type=huggingface data_name=conll2003 dataconfig=None subset=0 model_checkpoint=bert-base-cased task=token_classifier outputdir=./output traintag=0807 training=False total_epochs=4 save_every=2 batch_size=8 learningrate=2e-05
oneitem all keys: dict_keys(['id', 'tokens', 'pos_tags', 'chunk_tags', 'ner_tags'])
task token_classifier: {'LOC': {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1837}, 'MISC': {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 922}, 'ORG': {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1341}, 'PER': {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1842}, 'overall_precision': 0.0, 'overall_recall': 0.0, 'overall_f1': 0.0, 'overall_accuracy': 0.764084299758639}

NLP dataset
~~~~~~~~~~~~

GLUE, the General Language Understanding Evaluation benchmark (https://gluebenchmark.com/) is a collection of resources for training, evaluating, and analyzing natural language understanding systems.
https://huggingface.co/datasets/glue


IMDb Reviews: http://ai.stanford.edu/~amaas/data/sentiment/
The IMDB dataset contains 25,000 movie reviews labeled by sentiment for training a model and 25,000 movie reviews for testing it.

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