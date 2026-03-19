import pandas as pd 

# data=[100,120,140,160,180]

# series1=pd.Series(data)
# print(series1)

# series2=pd.Series(data,index=["a","b","c","d","e"])
# print(series2)

# print(series2.loc["b"])
# print(series2.iloc[1])
# print(series2.loc["c"])
# series2.loc["c"]=500

# print(series2.loc["c"])

# print(series2.iloc[0])
# print(series2.iloc[1])
# print(series2.iloc[2])
# print(series2.iloc[3])
# print(series2.iloc[4])

# data1=[100,120,140,160,180,200,220]
# series=pd.Series(data1,index=["a","b","c","d","e","f","g"])
# print(series[series>200])

# steps ={"day1":1241,"day2":1465,"day3":2350}
# sereis=pd.Series(steps)
# print(sereis)

# data={"name":["nirav","parthak","brocode"],"age":[13,18,19]}
# df=pd.DataFrame(data,index=["emp1","emp2","emp3"])
# print(df)
# print(df.loc["emp1"])
# print(df.loc["emp2"])
# print(df.loc["emp3"])

# df["language"]=["rust","python","java"]
# print(df)

# new_row=pd.DataFrame({"name":"harry","age":30,"language":"GO"},index=["emp4"])
# df=pd.concat([df,new_row])
# print(df)

# data={"name":["parth","bhargav","kiki","rkn"],"year":[1,1,2,0]}
# df=pd.DataFrame(data,index=[1,2,3,4])
# print(df)
# df["city"]=["delhi","chandigarh","delhi","udaipur"]
# print(df)

# new=pd.DataFrame({"name":["rusu","vedant"],"year":[3,3],"city":["pune","pune"]},index=[5,6])
# df=pd.concat([df,new])
# print(df)

# new=pd.DataFrame({"name":"rusu","year":3,"city":"pune"},index=[5])
# df=pd.concat([df,new])
# print(df)



# df=pd.read_csv("data.csv",index_col=["Name"])
# # print(df["No"])
# print(df.loc["Mewtwo"])

# df=pd.read_csv("data.csv")
# print(df.to_string())
# df=pd.read_csv("data.csv")
# print(df["Name"])
# print(df.iloc[:,1:4]

# print(df["Name"])
# print(df["Height"])

# print(df[["Name","Weight","Height"]])
# print(df.loc["Pikachu"]) error coz loc only index not nome soe lets set index a aname 

# df=pd.read_csv("data.csv",index_col=["Name"])
#loc for rows not for cloumns 
#for fcloumns we dont use loc 
#also iloc fo rnamemal index lik e0 1 23 4 5 

# print(df)
# print(df.loc["Pikachu"])

# print(df.loc["Moltres"])

# print(df.loc["Moltres",["Weight","Height"]])

# print(df.iloc[0:11:2])

# print(df.iloc[0:11,1:4])

df=pd.read_csv("data.csv")
# tall_poke=df[df["Height"]>2]
# print(tall_poke[["Name","Weight"]])

# heavy_poke=df[df["Weight"] >100]
# print(heavy_poke[["Name","Weight"]])

# legendary_poke=df[df["Legendary"]==1]
# print(legendary_poke)

# water_type=df[(df["Type1"]=="Water") | (df["Type2"]=="Water")]
# print(water_type)

# ff_pokemon=df[(df["Type1"] == "Fire")& (df["Type2"] == "Flying")]
# print(ff_pokemon)


# print(df.mean(numeric_only=True)
# print(df.max(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df["Height"].mean())
# print(df["Height"].max())
# print(df["Height"].min())
# print(df["Height"].sum())

# group=df.groupby("Type1")
# print(group["Height"].mean())
# print(group.count())
# print(group["Height"].max())

dfkd=pd.read_csv("fkedata.csv")
# print(dfkd)
# dfkd=dfkd.drop(columns=["Legendary","No","Type2"])
# print(dfkd)

# df=dfkd.dropna(subset=["Type2"])
# print(df.to_string())

# df=dfkd.fillna({"Type2":"none"})
# print(df.to_string())

# df["Type1"]=dfkd["Type1"].replace({"Grass":"GRASS","Fire":"FIRE"})
# print(df)

# df["Name"]=df["Name"].str.lower()
# print(df)

# dfkd["Legendary"]=dfkd["Legendary"].astype(bool)
# print(dfkd)

# dfkd=dfkd.drop_duplicates()
# print(dfkd)

dfkd=dfkd.isnull.sum()
print(df)