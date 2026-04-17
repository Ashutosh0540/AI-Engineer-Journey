import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

import pandas as pd

df = pd.read_csv("Day4/students.csv")

print("All Students:")
print(df)

print("\n Average Marks:",df["marks"].mean(), 2)
print("\nTop Students:")
top_su=df[df["marks"]>80]
print(top_su)
print("\nFailed Students:")
failed_stu=df[df["marks"]<40]
print(failed_stu)

df["status"]=df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print("\nWith Status:")
print(df)