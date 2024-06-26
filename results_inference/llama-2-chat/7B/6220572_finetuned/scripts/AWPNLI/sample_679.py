bought_coloring_books_premise = 48.0
given_away_coloring_books_premise = 34.0
given_away_more_coloring_books_premise = 3.0
remaining_coloring_books_hypothesis = 12.0

# the hypothesis refers to the number of coloring books left, which is also referenced in the premise
# compute the total number of coloring books left in the premise
total_coloring_books_premise = bought_coloring_books_premise - given_away_coloring_books_premise - given_away_more_coloring_books_premise
if remaining_coloring_books_hypothesis!= total_coloring_books_premise:
    # check if the number of coloring books left in the hypothesis contradicts the number of coloring books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
