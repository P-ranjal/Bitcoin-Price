#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from werkzeug.wrappers import Request, Response
from  flask import Flask, render_template, request
import pickle
import numpy as np
#from  bs4 import BeautifulSoup
import requests
import time
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def man():
    return render_template("home.html")
@app.route('/predict', methods=['POST'])
def home():
    #url='https://www.google.com/search?q=bitcoin+price'
    #HTML=requests.get(url)
   # soup=BeautifulSoup(HTML.text,'html.parser')
    #text=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    if request.method=='POST':
        model = pickle.load(open('regt.pkl', 'rb'))
        data1 = request.form['a']
        data2 = request.form['b']
        data3 = request.form['c']
        data4 = request.form['d']
        data1=float(data1)
        data2=float(data2)
        data3=float(data3)
        data4=float(data4)
        arr = [[data1, data2, data3, data4]]
        pred = model.predict(arr)
        a="The Predicted One"
       # b="The Current Value"
        l=[pred[0],a]
    return render_template('after.html',l=l)
if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)


# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:





# In[ ]:




