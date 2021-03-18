#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def abc():
    return render_template('prime.html')

@app.route('/detail',methods=['GET','POST'])
def xyz():
    if request.method=='POST':
        x=int(request.form['a'])
        l=[]
        for i in range(1,x+1):
            c=0
            for j in range(1,i+1):
                if i%j==0:
                    c=c+1
            if c==2:
                l.append(i)
    return render_template('prime.html',answer=l)

if __name__=='__main__':
    app.run()
                


# In[ ]:




