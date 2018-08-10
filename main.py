import numpy as np
import pandas as pd
print("Ani's first code with python")
temp = [[1],[2],[3],[4],[5],[6],[7],[8]]
print(temp)

df = pd.DataFrame(temp)
"""
block comment
"""
print(df.iloc[5, 0])

df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
#print(df)
df.columns = ['cakes']
df['cakes'] *= 4
print(df)

def func():
    try:
        print("this is a test\n")
        if not temp:            #comment example, go into if temp is empty
            print("temp is empty")
        elif temp[0] == 1:
            print("temp is 4 long")
        else:
            print("temp is a list")
        i = 0
        for i in temp:
            i+=1
            temp.pop()
    except Exception as e:
        print("you messed up")

if __name__ == "__main__":
    func()