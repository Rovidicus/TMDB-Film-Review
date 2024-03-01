# Movie Reviews NLP Analysis

### Goal: to decipher from review text whether a rating will be positive or negative

##### Dataset source: [movie_reviews_v2.csv](https://github.com/Rovidicus/Data-Enrichment-Project/files/14460822/movie_reviews_v2.csv)
##### This product uses the TMDB API but is not endorsed or certified by TMDB.
![TMDB](https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_1-5bdc75aaebeb75dc7ae79426ddd9be3b2be1e342510f8202baf6bffa71d7f5c4.svg)

### Exploring the dataset revealed 27 duplicates which were removed and 1196 nulls in our ratings of a total dataset of 8650. Null rows were dropped along with the three id columns.

### We really want to hone in on very positive and very negative reviews to see the difference in language.
### To do this we created 'high' and 'low' filters for ratings at and above 9.0 and at and below 4.0 respectively.
### Defining a custom SpaCy term that removes 'parse' and 'ner' saved a lot in data processing time.

### With a batch preprocess custom function, we made columns for tokens and lemmas, each with joined columns for later analytical dissection.

## WordCloud

### Using a default word cloud can turn up many words that aren't caught with default stopwords. Once I could see word distribution better, I made a custom list of stop words to better illuminate more interesting review words.

![High Review Word Cloud](https://github.com/Rovidicus/Data-Enrichment-Project/blob/main/Data/Images/high_cloud.png) ![Low Review Word Cloud](https://github.com/Rovidicus/Data-Enrichment-Project/blob/main/Data/Images/low_cloud.png)

### There appears a big vocabulary parallel with positive and negative reviews so far. Character, story and people recur frequently. Words like "bad", "try", and "end" make up many negative reviews while "great" and "love" are in positives.
### Word clouds in this case weren't too revealing once obvious stop words were removed.

## Frequency Distribution

### Using our lemmas datasets, we got lineplots of word distributions across reviews.

![Low Review Frequency Distribution](https://github.com/Rovidicus/Data-Enrichment-Project/blob/main/Data/Images/low_freq_dist.png)

![High Review Frequency Distribution](https://github.com/Rovidicus/Data-Enrichment-Project/blob/main/Data/Images/high_freq_dist.png)

### Character and story are emphasized in both graphs.

## Bigrams

### It can be helpful to spot words that occur together frequently to see correlations

| ('high reviews', 'Words')   |   ('high reviews', 'Raw Freq') | ('low reviews', 'Words')    |   ('low reviews', 'Raw Freq') |
|:----------------------------|-------------------------------:|:----------------------------|------------------------------:|
| ('comic', 'book')           |                    0.000436441 | ('final', 'rating')         |                   0.00112837  |
| ('special', 'effects')      |                    0.000436441 | ('rating', '★')             |                   0.00112837  |
| ('star', 'wars')            |                    0.000393512 | ('★', '★')                  |                   0.0010314   |
| ('sci', 'fi')               |                    0.000357738 | ('finished', 'product')     |                   0.000846277 |
| ('feel', 'like')            |                    0.000350583 | ('appeal', 'poor')          |                   0.000837462 |
| ('action', 'movie')         |                    0.000343429 | ('poor', 'finished')        |                   0.000837462 |
| ('watch', 'movie')          |                    0.00031481  | ('things', 'appeal')        |                   0.000837462 |
| ('john', 'wick')            |                    0.000307655 | ('★', 'things')             |                   0.000837462 |
| ('real', 'life')            |                    0.000307655 | ('special', 'effects')      |                   0.000643523 |
| ('long', 'time')            |                    0.0003005   | ('feels', 'like')           |                   0.000537739 |
| ('<', '>')                  |                    0.000293345 | ('★', '½')                  |                   0.000528923 |
| ('best', 'movies')          |                    0.000279036 | ('avoid', 'possible')       |                   0.000511293 |
| ('spider', 'man')           |                    0.000271881 | ('boring', 'disappointing') |                   0.000511293 |
| ('science', 'fiction')      |                    0.000257572 | ('disappointing', 'avoid')  |                   0.000511293 |
| ('best', 'films')           |                    0.000250417 | ('½', 'boring')             |                   0.000511293 |
| ('★', '★')                  |                    0.000250417 | ('final', 'rating:')        |                   0.000502477 |
| ('good', 'movie')           |                    0.000243262 | ('rating:', '★')            |                   0.000502477 |
| ('spoiler', 'free')         |                    0.000243262 | ('looks', 'like')           |                   0.000405508 |
| ('action', 'sequences')     |                    0.000236107 | ('good', 'movie')           |                   0.000352616 |
| ('felt', 'like')            |                    0.000228952 | ('star', 'wars')            |                   0.000352616 |

### Low reviews paired final and rating frequently, with boring and disappointing. The high reviews really talked up the genres and specific brands like Star Wars and John Wick.

## Sentiment Analysis

### We contrasted positive reviews with negative sentiment score and vice versa to see what it revealed.
### Positive sentiments may be boosted by catchphrases in otherwise negative reviews, such as "GREAT CAST", "attractive women", "high-praise" and "fun scenes".
### Like the negative reviews, catchphrases turn the balance like "most people don't care for" and "death sentence". Of note also is reviewers writing synapses of the plots' exciting parts and character quotes which in isolation may be interpreted negative. Sentiment analysis may not understand context this far yet.

# Reflection
## Were one to make a successful movie, there could be some lessons to extrapolate here:
1. Story and character are frequently brought up in reviews, positive and negative. Make them memorable not formulaic.
2. Based on our bigrams, reviewers appreciate films true to their genres (action, sci fi). Boring and not being finished recur for negatives.
3. Positive reviews quote characters and scenes while negative reviews emphasize the films' forgettability.

