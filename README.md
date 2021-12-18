## Dataset:
- [Steamspy](https://steamspy.com/api.php): We use dataset that we crawling from Steamspy since the API is free and it have positive rating and negative rating. This dataset we use for TFIDF and Hybrid recommend
- [Steam video game hours played](https://www.kaggle.com/tamber/steam-video-games/data): We use the dataset that contain hours that users spend for their game. This dataset we use for SVD and Hybrid recommend
## Preprocessing:
- [Steamspy](https://steamspy.com/api.php): this dataset does not contain game description and game image link. So first we combine steam url with id column in this dataset and set this column as `links`. Next we crawling game description([linkhere]())
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
