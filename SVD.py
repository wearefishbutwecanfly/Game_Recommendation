import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate
from content_based import df, content_based_recommend

df_rating = pd.read_csv("rating.csv")
user_rating = pd.read_csv("user_rating.csv")
# user_rating.columns = ["ID", "User_ID","Game_id", "Game_name","Rating"]

full_df_rating = pd.concat([user_rating[["User_ID","Game_name","Rating"]],df_rating[["User_ID","Game_name","Rating"]]])

# Load data from full_df_rating
reader = Reader()
data = Dataset.load_from_df(full_df_rating[['User_ID', 'Game_name','Rating']], reader)

svd = SVD()

print("Training SVD")
trainset = data.build_full_trainset()
svd.fit(trainset)
print("Complete traing SVD")

# Tạo hàm SVD function 
def SVD(User_ID, max_number_predict, max_number_database, database):
    list_game_content_based = database["Game_name"][:max_number_database]
    df_test = {"User_ID": User_ID,"Game_index":[], "Game_Predict":[],"Est":[]}
    for i in list_game_content_based:
        df_test['Game_Predict'].append(i)
        df_test['Game_index'].append(df[df['Game_name']==i].index[0])
        df_test["Est"].append(svd.predict(User_ID, i).est)

    df_test = pd.DataFrame(df_test)
    df_test = df_test.sort_values(by=['Est'], ascending=False)[:max_number_predict]

    return df_test

# Tạo hàm hybrid function 
def hybrid(User_ID,Game_index, Game_name, max_number_content, max_number_predict):
    list_game_content_based = df.iloc[content_based_recommend(Game_index,max_number_content)]["Game_name"]
    df_test = {"User_ID": User_ID,'Game':Game_name,"Game_index":[], "Game_Predict":[],"Est":[]}
    for i in list_game_content_based:
        df_test['Game_Predict'].append(i)
        df_test['Game_index'].append(df[df['Game_name']==i].index[0])
        df_test["Est"].append(svd.predict(User_ID, i).est)

    df_test = pd.DataFrame(df_test)
    df_test = df_test.sort_values(by=['Est'], ascending=False)[:max_number_predict]

    return df_test


# list_game_hybrid = hybrid(1, df["Game_name"][0], 20)

# print(list_game_hybrid.sort_values(by=['Est'], ascending=False)[:10])

# print("----------------------------------------------------------------")
# list_game_SVD = SVD(2, 20)

# print(list_game_SVD)