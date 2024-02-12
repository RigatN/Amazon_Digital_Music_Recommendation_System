
# Steam Games Recommendation System


# ![amazon](https://github.com/RigatN/Amazon_Digital_Music_Recommendation_System/main/Images/cover.PNG)

## Overview

In this project, I aim to develop a collaborative filtering recommendation system tailored for Amazon digital music. By leveraging user interactions with music items, such as ratings or purchase histories, the system will analyze patterns and similarities among users and items to generate personalized music recommendations. The project will involve preprocessing the Amazon digital music dataset, training various collaborative filtering models, and evaluating their performance using metrics such as accuracy and coverage. Ultimately, the goal is to deploy a robust recommendation system that enhances the user experience by providing relevant and personalized music suggestions based on their preferences and behaviors.


## Business Understanding

In the realm of digital music, enhancing user engagement and satisfaction is paramount for online platforms like Amazon. By implementing a collaborative filtering recommendation system, Amazon aims to provide users with personalized music recommendations that resonate with their tastes and preferences. This not only fosters a more enjoyable user experience but also increases user retention and loyalty. Additionally, by surfacing relevant music content, Amazon can potentially boost sales and revenue through increased music streaming or purchases. Understanding user preferences and behavior through collaborative filtering enables Amazon to tailor its offerings and marketing strategies, ultimately leading to a more successful and customer-centric digital music platform.

## Data Understanding and Preprocessing

The dataset, was pulled from a compiled dataset of Amazon.The data set can be found in [here](https://nijianmo.github.io/amazon/index.html).The data contains two zipped JSON files: the review and metadata. Due to the large size of the data, GitHub couldn't allow me to upload it here, but it can be found on the link I provided above.

Given that the rating distribution is not normal, it could influence our recommendation system model. Hence, we'll generate a new normalized rating column by subtracting the average rating of each reviewID from the original rating.

# ![review](https://github.com/RigatN/Amazon_Digital_Music_Recommendation_System/blob/main/Images/distribution_of_rating.png)


# Modeling and Evaluation
We are building a Collaboritive Recommendation System with a python package called `surprise` here is a [link](https://surprise.readthedocs.io/en/stable/) to the documentation. So we started with a baseline model using `Normal Predictor` which we will use to compare results to our optimized final model. Through an iterative process we tried a few different models within the surprise library such as `SVD`, `KNNWithMeans`, and `SVD++`. The metrics we used with cross validation to evaluate our models is RMSE (root mean squared error) and MAE (mean absolute error).

<<<<<<< HEAD
<<<<<<< HEAD
# ![EDA](https://github.com/pyamin1878/Steam-Games-Rec-System/blob/main/Images/EDA.PNG)
=======
#### Normal Predictor 
![Alt text](Images/Normal_Predictor_Results.png)
>>>>>>> main
=======


#### Normal Predictor 
![Alt text](Images/Normal_Predictor_Results.png)

>>>>>>> main

#### SVD
![Alt text](Images/SVD_Results.png)

#### KNNWithMeans
![Alt text](Images/KNNWithMeans_Results.png)

### SVD++ 

#### Final Optimized Model

We used `GridSearchCV` to optimize our final model SVD++ which had the best performance and lowest RMSE and MAE on the testset. Hyperparameters as well as the best RMSE score are provided. 

![Alt text](Images/SDVpp_Results.png)




## Next Step

In the next phase of the project, users will have the opportunity to input their unique user_id through API calls, enabling the system to provide personalized game recommendations tailored to their gaming preferences. This interactive feature enhances the user experience by delivering targeted suggestions based on individual gaming histories. By leveraging API functionality, the recommendation system ensures a dynamic and user-centric approach, fostering greater engagement and satisfaction within the gaming community.

Stable Deployment for our model with hf spaces or a full web application.



## Repo Structure

```
├── Images
├── data
├── notebooks
├── .gitignore
├── License
├── README.md
├── Recommendation_System.ipynb -------------> Final Notebook
├── svdpp_model.pkl ---------------->          Final Model
```
## Citations

[Kaggle Notebook](https://www.kaggle.com/code/simonprevoteaux/steam-game-analysis/notebook)
