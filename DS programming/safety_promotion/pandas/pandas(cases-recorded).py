import pandas as pd

d = pd.read_csv("C:/Users/User/Desktop/suss/specialised dip/Introduction to programming for DS/CA02/cases-recorded-for-selected-major-offences.csv")
df = pd.DataFrame(d)
d_name = "cases-recorded-for-selected-major-offences.csv"
print("\nDataset loaded: {}\n".format(d_name))
print("Shape of the dataset: \n{}\n".format(d.shape))
print("Index of the dataset: \n{}\n".format(d.index))
print("Total number of non-NA values in this dataset: \n{}\n".format((df.count())))
print("Summary of the dataset:")
print(df.info())
print("\nDescriptive statistical summary of the dataset:")
print(df["value"].describe())