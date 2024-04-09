books_bought_premise = 48.0
books_given_away_premise = 34.0
books_given_away_hypothesis = 3.0
books_left_hypothesis = 11.0

# compute the total number of books given away in the premise
total_books_given_away_premise = books_given_away_premise + books_given_away_hypothesis

# check if the number of books left in the hypothesis contradicts the estimate of books given away in the premise
if books_left_hypothesis < total_books_given_away_premise:
    label = "contradiction"
elif books_left_hypothesis > total_books_given_away_premise:
    # check if the number of books left in the hypothesis contradicts the number of books given away in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
