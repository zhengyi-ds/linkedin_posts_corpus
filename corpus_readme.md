# Corpus Details

## 1. Source of the Corpus
- **Original Data:** [Kaggle: “LinkedIn Influencers Data”](https://www.kaggle.com/datasets/shreyasajal/linkedin-influencers-data)

## 2. Location of Collected Corpus
- **Storage Path:** [`data/linkedIn_data.csv`](data/linkedIn_data.csv)

## 3. About the Dataset (As per Source of the Corpus)
This dataset contains LinkedIn Influencers' post details and other details (post-dependent as well as independent) per post. This dataset can be used to analyze LinkedIn reach based on post content and related account details.

This dataset is great for Exploratory Data Analysis and NLP tasks.

The data was scraped using **BeautifulSoup** and **Selenium**.  
**Last updated:** 15th Feb, 2021.


## 4. Corpus Format and Metadata (Source Corpus)
- **Format:** CSV (Comma-Separated Values)
- **Columns Include:**
  - `name` (Influencer’s name)
  - `headline` (The header of their linkedin Profile)
  - `location` (Influencer's location as provided on linkedin)
  - `followers` (Number of followers the influencer has)
  - `connections` (Number of LinkedIn connections)
  - `about` (bio of the influencer's profile)
  - `time_spent` (time spent since uploading the post as on 15 Feb 2021)
  - `content` (Post content)
  - `content_links` (Links included in the post)
  - `media_type` (Type of media attached to the post, e.g., image, video, article, etc)
  - `media_url` (URL of the media file)
  - `num_hashtags` (Number of hashtags used in the post)
  - `hashtag_followers` (Number of followers associated with the hashtags used)
  - `hashtags` (List of hashtags used in the post)
  - `reactions` (No.of post reactions)
  - `comments` (Number of comments on the post)
  - `views` (Number of views on the post)
  - `votes` (In case the post type is poll, the total number of votes cast on the poll)

The columns `name`, `headline`, `location`, `about` will be removed from the final corpus(1600 documents) to keep anonymity of the user, and `votes`, `media_url` will be removed because we wouldn't be using these columns in our final corpus.    


## 5. Total Number of Documents 
-  Source corpus contains approximately *34,012* rows (each row can be considered one “document” or entry). Final corpus (filtered) will contain *1600* rows. 

## 6. Total Amount of Text
- We will annotate the `content` column in the final corpus (1600 documents). The total tokens are estimated at around 95763 tokens.

## 7. Known Problems with the Corpus
- The `content` column in the source corpus has 2772 duplicate entries. In our final corpus of 1600 documents there will be 0 duplicates.
- `media_type` column contains posts that are not relevant for our task. Like `poll` had incomplete data without context, so we filtered only the relevant media types. 
- Limited **noise** in user-generated columns (e.g., special characters like $ or symbols that are not relevant).
- There are 2016 missing values in Content (posts) Column in original (source) data.

## 8. License
[`Database: Open Database, Contents: Database Contents`](https://opendatacommons.org/licenses/dbcl/1-0/)
