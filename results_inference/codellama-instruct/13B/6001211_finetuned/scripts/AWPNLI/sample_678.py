bought_books_premise = 48.0
gave_away_books_premise = 34.0
additional_give_away_books_premise = 3.0
left_books_hypothesis = 11.0

# the hypothesis refers to the number of coloring books left, which can be computed from the premise
# compute the total number of coloring books left in the premise
total_books_left_premise = bought_books_premise - gave_away_books_premise - additional_give_away_books_premise
if left_books_hypothesis!= total_books_left_premise:
    # check if the number of coloring books left in the hypothesis contradicts the number of coloring books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
