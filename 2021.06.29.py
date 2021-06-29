import pandas as pd

file = "C:/Users/hyesu/Downloads/train.csv"
df = pd.read_csv(file)

print(df.head())
print(df.tail())
print(df.info())
print(df.isna())
print(df.describe(include="all"))       #기본통계정보
print(df.corr())
print(df.mean())
print(df.groupby("Survived").mean())
print(df.groupby(["Sex", "Survived"]).mean())

print(df["Survived"])
print(df.Survived)

print(df.loc[0])
print(df.loc[0, "Name"])

print(df.iloc[0])
print(df.iloc[0:5, 1:4])

print(df[["Name", "Age", "Sex", "Survived"]])

mask = (df.Sex == "female")
print(mask)
print(df[mask])

df["new"] = 0
print(df.head())

df["family"] = df["SibSp"] + df["Parch"]
print(df.head())

# df = df.drop(labels="new", axis=1)
df.drop(columns=["new", "family"], inplace=True)

print(df.head())

np.random.seed(0)
data = np.random.randn(len(df))
standard = pd.Series(data, name="standard")
print(standard)
total = pd.concat(objs=[df, standard], axis=1)
print(total)

data = np.arange(len(df.columns)).reshape(1, -1)
number = pd.DataFrame(data, columns=df.columns)
print(number)
df2 = pd.concat([df, number], axis=0)
print(df2)

print(df2.reset_index(drop=True))

df = df.rename({"Name": "이름"}, axis=1) # df.rename({"Name": "이름"}, axis=1, inplace=True)
print(df)
print(df.info())


# p 223 부터
