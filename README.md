# GAME RECOMMENDATION SYSTEM

You can read report for more detail about functions and implementation: [link to report](https://docs.google.com/document/d/1zXZVXTK1vfmtwWJcHsbZ1BJ2liK2q2STaIc3XFUC1PA/edit?fbclid=IwAR1f8pU0R8Z7p8ThlSF6UeJfqsVU-FUc1JB8DihSyytc5WKt-GKVtusXsIc#)

## Introduction:
From year to year, one thing that we can not agree more on is that most people around the world love playing games, especially video games. We realized that playing video games is a part of childhood for most of us, so in the course "Decision Support System", we built this small project called "Game Recommendation System" to find out the most suitable game for them with as high accuracy as possible. In this project, we built 4 basic functions to suggest games for users. The first function is games recommendation based on the user's voting rate. The second function is games recommendation based on the game description by using the content-based filtering technique. The third function is games recommendation based on the user's game taste, which is measured by the played time for each game of the user, by using the collaborative filtering technique. The last one is the combination of the second and the third function to recommend the most suitable games to the specific user. The fourth function is operated by applying the hybrid technique and from that, we consider this function as the one for the "oriented-user" purpose. In addition, we also implemented a web application for the user interface that could help users interact with our recommendation system. Through this project, we knew how the recommendation system works and understood the algorithms behind how to operate the system. Here is the MVC architecture that demonstrates how our system works:
<p align="center">
  <img src="https://user-images.githubusercontent.com/58814046/146629404-d6a99ac5-81ea-47e5-b76a-ab830e270a0a.png" alt="MVC">
   <p align="center">Figure 1: The MVC architecture</p>
</p>

 
## Dataset:
- [Steamspy](https://steamspy.com/api.php): We use dataset that we crawling from Steamspy since the API is free and it have positive rating and negative rating. This dataset we use for TFIDF and Hybrid recommend and we name it `steam_api.csv`
- [Steam video game hours played](https://www.kaggle.com/tamber/steam-video-games/data): We use the dataset that contain hours that users spend for their game. This dataset we use for SVD and Hybrid recommend and we name it `rating.csv`
- user_rating.csv: We use this dataset for SVD and Hybrid recommend for current user. Because `rating.csv` does not contain our project user so we must merge `user_rating.csv` with `rating.csv`for SVD training process.
## Preprocessing:
### 1. Clean data
- [Steamspy](https://steamspy.com/api.php): this dataset does not contain game description and game image link. So first we combine steam url with id column in this dataset and set this column as `links`. Next we crawling game description([linkhere](https://colab.research.google.com/drive/131-T5mH6c8jFx8WDhqa093IiAliPpjVC?usp=sharing)) and crawling game image ([linkhere](https://colab.research.google.com/drive/1k5yrE1RmlN1KbD4d0z2NZtDUV7Hf-0NM?usp=sharing)). Next we remove `NaN` value in these both columns and `duplicate` in dataset. Finally, we fill NaN of `publisher` with value in `developer` at same row and the same for `developer` so now we can use `printable` in `string library` to remove non-Ascii letters.
- [Steam video game hours played](https://www.kaggle.com/tamber/steam-video-games/data): We remove game name in this dataset that not in game name of Steamspy and Merge interaction `purchased` and `play` so it just contain user who bought and play that game.
### 2. Convert Steam video game hours played to Rating dataset
- We use the paper [Estimated Rating Based on Hours Played for Video Game Recommendation](https://www.researchgate.net/publication/330249306_Estimated_Rating_Based_on_Hours_Played_for_Video_Game_Recommendation) from [ResearchGate] to compute `Frequency` and `Rating`. Here is our result, to more detail, you can read report
 ![image](https://user-images.githubusercontent.com/58814046/146628417-35e70dee-52fd-4993-b305-101c2bcb6bba.png)
 
## Recommendation Algorithms:
- [TFIDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) : We use this algorithm for Content based recommend. In our project, the list of game `GAME HAVE SIMILAR CONTENT` in detail of game pages is the prediction of this algorithm. 
- [SVD](https://surprise.readthedocs.io/en/stable/matrix_factorization.html) : 
   -  When login to our project, we see the TOP GAME BY POSITIVE SCORE column, this column we use SVD to calculate the estimation of the current user with all games in the dataset and then show list games has the highest estimation score.
   -  Next, when click to game to go to detail page, the IF YOU LIKE THIS GAME YOU MIGHT LIKE THESE column is we use the hybrid with combine TFIDF and SVD so it will calculate estimate score from list game that TFIDF predict and then show games have highest estimation score.
## How to run project:
1. Create the virtual environment: `python3 -m venv tutorial-env`
2. Active the Script
  - On Windows: `tutorial-env\Scripts\activate.bat`
  - On MacOS: `tutorial-env\Scripts\activate.bat`
3. Install all necessary libraries: `pip install -r requirements.txt`
4. Run the program `python main.py`. After the program runs successfully, access this address `http://127.0.0.1:2300/` to get experience with the web application.
## File explanation
1. main.py: run `Python Flask Application`
2. init.py: set up `SQLAlchemy` and `Python Flask Application` and `register_blueprint` for `view.py`
3. view.py: contain `address` for `Python Flask Application` which are: login page, register page, index page, home page, detail page.
4. models.py: contain SQL models which are: `User` and `Rating`. 
- `User`: user has `id`, `username`, `password`, `ratings`.`id` must be unique and `username` cannot duplicate
- `Rating`: rating has `id`, `userid`, `gameid`, `gamename`, `rating`. A rating must have unique `id` and if a user has already `rate` that game, the `rating` will update
5. content_based.py: contain `TFIDF model` and the training dataset is `steam_api.csv`. It contain one function:
- `content_based_recommend`: return list indexs of games that TFIDF predict when input `game index of game we want predict` and `the number contain based will recommend`
6. SVD.py: contain `SVD models` and the training dataset is merged by `rating.csv` and `user_rating.csv`. It have two function
- `SVD`: it return list of game when input `user id`, `number game the function will return`, `number of games we want to SVD calculate`,`database we want SVD use for calculate`
- `Hybrid`: it return list of game when input `user id`,`game index for content_based_recommend`, `number that contain based will recommend`,`number game the function will return`
7. templates:
- `Login System`: base.html, index.html, login.html, register.html
- `Home Page`: home.html
- `Detail Page`: detail.html
8. static: contain `css`, `javascripts`,`fonts`,`slick`
## Troubleshooting
- `Reset dataset`: Delete `users.db` to reset all account and remove all data in `user_rating.csv` NOT DELETE IT and just remain headers ID,User_ID,Game_id,Game_name,Rating
- `Pip install suprise error` or `Pip install -r requirements.txt`: I haven't has this error yet but my friend solve it by download Microsoft C++ Build Tools
