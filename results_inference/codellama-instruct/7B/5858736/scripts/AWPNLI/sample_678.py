bought_coloring_books_premise = 48.0
given_away_coloring_books_premise = 34.0
given_away_more_coloring_books_premise = 3.0
total_coloring_books_premise = bought_coloring_books_premise - given_away_coloring_books_premise - given_away_more_coloring_books_premise

# the hypothesis refers to the number of coloring books that Faye would have left
# compute the total number of coloring books that Faye would have left
total_coloring_books_hypothesis = total_coloring_books_premise - given_away_more_coloring_books_premise

if total_coloring_books_hypothesis!= 11.0:
    # check if the number of coloring books in the hypothesis contradicts the number of coloring books that Faye would have left
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
