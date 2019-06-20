#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
from bs4 import BeautifulSoup
print("How do you fell now? -- 1.excited  2.nothing  3.sad")
result_emotion = input('選択:')
if result_emotion =='1':
    con = sqlite3.connect("./karaok.db")
    cursor = con.cursor()
    res = cursor.execute("SELECT name FROM songs WHERE emotion > 0").fetchall()[::-1]
    for i in res:
        print("".join(i))
elif result_emotion =='2':
    con = sqlite3.connect("./karaok.db")
    cursor = con.cursor()
    res = cursor.execute("SELECT name FROM songs  WHERE emotion = 0").fetchall()
    for l in res:
        print("".join(l))
else:
    con = sqlite3.connect("./karaok.db")
    cursor = con.cursor()
    res = cursor.execute("SELECT name FROM songs  WHERE emotion < 0").fetchall()
    for m in res:
        print("".join(m))


# In[15]:


print("気になる歌あった--yes 、have no idea")
result_name = input()
if result_name=="yes":
#     print("曲名を入力してください")
    name = input("曲名を入力してください:")
    con = sqlite3.connect("./karaok.db")
    cursor = con.cursor()
    res = cursor.execute("SELECT lytic FROM songs WHERE name =?", (name,)).fetchone()[0]
    print('========================================\n')
    print(res)
else:
    print("好きな単語を選んでください")
    if result_emotion =='1':
        con = sqlite3.connect("./karaok.db")
        cursor = con.cursor()
        res = cursor.execute("SELECT special FROM songs WHERE emotion > 0").fetchall()
        for i in res:
            print("".join(i))
    elif result_emotion =='2':
        con = sqlite3.connect("./karaok.db")
        cursor = con.cursor()
        res = cursor.execute("SELECT special FROM songs  WHERE emotion = 0").fetchall()
        for l in res:
            print("".join(l))
    else:
        con = sqlite3.connect("./karaok.db")
        cursor = con.cursor()
        res = cursor.execute("SELECT special FROM songs  WHERE emotion < 0").fetchall()
        for m in res:
            print("".join(m))
    point_word = input("単語を入力中...")
    con = sqlite3.connect("./karaok.db")
    cursor = con.cursor()
    res = cursor.execute("SELECT name,lytic FROM songs WHERE special =?", (point_word,)).fetchall()
    for n in res:
        print("\n曲名:"+"\n========================================\n".join(n))
    


# In[ ]:




