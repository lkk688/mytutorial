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

SQuAD: https://rajpurkar.github.io/SQuAD-explorer/

.. code-block:: console 

    E:\Dataset\NLPdataset\squad> wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json -O train-v2.0.json