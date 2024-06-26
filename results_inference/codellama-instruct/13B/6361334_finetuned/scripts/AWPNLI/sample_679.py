bought_coloring_books_premise = 48.0
gave_away_coloring_books_premise = 34.0
gave_away_more_coloring_books_premise = 3.0
left_coloring_books_hypothesis = 12.0

# the hypothesis refers to the number of coloring books left, which are also mentioned in the premise
# compute the total number of coloring books given away from the premise
total_given_away_coloring_books_premise = gave_away_coloring_books_premise + gave_away_more_coloring_books_premise
# compute the total number of coloring books bought from the premise
total_bought_coloring_books_premise = bought_coloring_books_premise - total_given_away_coloring_books_premise
if left_coloring_books_hypothesis!= total_bought_coloring_books_premise:
    # check if the number of coloring books left in the hypothesis contradicts the number of coloring books bought from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
