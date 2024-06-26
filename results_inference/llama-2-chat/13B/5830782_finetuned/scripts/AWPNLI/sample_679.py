bought_coloring_books_premise = 48.0
gave_away_coloring_books_premise1 = 34.0
gave_away_coloring_books_premise2 = 3.0
left_coloring_books_hypothesis = 12.0

# the hypothesis refers to the number of coloring books left, which are also mentioned in the premise
# compute the number of coloring books left in the premise
left_coloring_books_premise = bought_coloring_books_premise - gave_away_coloring_books_premise1 - gave_away_coloring_books_premise2
if left_coloring_books_hypothesis!= left_coloring_books_premise:
    # check if the number of coloring books left in the hypothesis contradicts the number of coloring books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
