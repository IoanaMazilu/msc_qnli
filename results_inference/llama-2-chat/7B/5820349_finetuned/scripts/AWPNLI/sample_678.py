bought_books_premise = 48.0
given_away_books_premise = 34.0
remaining_books_hypothesis = 11.0

# the hypothesis refers to the number of coloring books left, which is also mentioned in the premise
# compute the remaining number of coloring books in the premise
remaining_books_premise = bought_books_premise - given_away_books_premise
if remaining_books_hypothesis!= remaining_books_premise:
    # check if the number of remaining books in the hypothesis contradicts the number of remaining books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
