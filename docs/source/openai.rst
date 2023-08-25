OpenAI
======

OpenAI quickstart application
------------------------------
https://platform.openai.com/docs/quickstart/add-some-examples

.. code-block:: console

    (mypy310) lkk@Alienware-LKKi7G8:~/Developer$ git clone https://github.com/openai/openai-quickstart-python.git
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/openai-quickstart-python$ ls -al
    total 44
    drwxr-xr-x  5 lkk lkk 4096 Aug 20 12:31 .
    drwxr-xr-x 16 lkk lkk 4096 Aug 20 12:31 ..
    -rw-r--r--  1 lkk lkk  162 Aug 20 12:31 .env.example
    drwxr-xr-x  8 lkk lkk 4096 Aug 20 12:31 .git
    -rw-r--r--  1 lkk lkk  115 Aug 20 12:31 .gitignore
    -rw-r--r--  1 lkk lkk 1063 Aug 20 12:31 LICENSE
    -rw-r--r--  1 lkk lkk 1210 Aug 20 12:31 README.md
    -rw-r--r--  1 lkk lkk  940 Aug 20 12:31 app.py
    -rw-r--r--  1 lkk lkk  413 Aug 20 12:31 requirements.txt
    drwxr-xr-x  2 lkk lkk 4096 Aug 20 12:31 static
    drwxr-xr-x  2 lkk lkk 4096 Aug 20 12:31 templates
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/openai-quickstart-python$ cp .env.example .env
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/openai-quickstart-python$ nano .env
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/openai-quickstart-python$ pip install -r requirements.txt
    $ flask run