import pandas as pd

d = pd.read_csv("C:/Users/User/Desktop/suss/specialised dip/Introduction to programming for DS/CA02/causes-of-accidents-by-severity-of-injury-sustained.csv")
df = pd.DataFrame(d)
d_name = "causes-of-accidents-by-severity-of-injury-sustained.csv"
print("\nDataset loaded: {}\n".format(d_name))
print("Shape of the dataset: \n{}\n".format(d.shape))
print("Index of the dataset: \n{}\n".format(d.index))
print("Total number of non-NA values in this dataset: \n{}\n".format((df.count())))
print("Summary of the dataset:")
print(df.info())
print("\nDescriptive statistical summary of the dataset:")
print(df["number_of_accidents"].describe())


