Streamlit
==========

Installation
--------------
https://docs.streamlit.io/

.. code-block:: console

    (mypy310) lkk@Alienware-LKKi7G8:~/Developer$ pip install streamlit
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer$ streamlit hello #run demo in browser
    streamlit run your_script.py [-- script args]

"st.write()": which can be used to write anything from text to tables. Streamlit supports "magic commands," which means you don't have to use st.write() at all!

Scripts use the Streamlit cache to avoid recomputing expensive functions, so updates happen very fast
    * "st.cache_data" is the recommended way to cache computations that return data
    * "st.cache_resource" is the recommended way to cache global resources like ML models or database connections – unserializable objects that you don’t want to load multiple times. 

Streamlit apps can contain multiple pages, which are defined in separate .py files in a pages folder.

References
-----------
Run a Streamlit App with Google Colab Notebook: https://alphasec.io/run-a-streamlit-app-with-google-colab-notebook/

https://github.com/mmz-001/knowledge_gpt/tree/main

https://alphasec.io/prototype-langchain-flows-visually-with-langflow/

https://alphasec.io/persistent-ai-chat-bots-with-langchain-and-steamship/

https://alphasec.io/deploy-your-own-ai-chat-bot-using-openai-and-vercel/

https://www.langchain.com/
LangChain is a framework for developing applications powered by language models. 

conda install langchain -c conda-forge
pip install langchain[llms]
pip install openai
https://python.langchain.com/docs/get_started/quickstart