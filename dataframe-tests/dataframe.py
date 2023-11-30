import pandas as pd

data_fake = {"teste": [],
             "teste2": []}

data = {"Name": ["Anna", "Bob", "Charlie", "Diana", "Eric"],
        "Age": [20, 34, 23, None, 33],
        "Gender": ["f", "m", "m", "f", "m"],
        "Job": ["Programmer", "Writer", "Cook", "Programmer", "Teacher"]}

df = pd.DataFrame(data)
print(df)


