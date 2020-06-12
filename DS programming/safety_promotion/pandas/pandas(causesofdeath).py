import pandas as pd

d = pd.read_csv("C:/Users/User/Desktop/suss/specialised dip/Introduction to programming for DS/CA02/principal-causes-of-death.csv")
df = pd.DataFrame(d)
d_name = "principal-causes-of-death.csv"
print("\nDataset loaded: {}\n".format(d_name))
print("Shape of the dataset: \n{}\n".format(d.shape))
print("Index of the dataset: \n{}\n".format(d.index))
print("Total number of non-NA values in this dataset: \n{}\n".format((df.count())))
print("Summary of the dataset:")
print(df.info())
print("\nDescriptive statistical summary of the dataset:")
print(df["percentage_deaths"].describe())


