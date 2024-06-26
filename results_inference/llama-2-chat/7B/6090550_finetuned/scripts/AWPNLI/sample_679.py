coloring_books_bought = 48.0
coloring_books_given_away = 34.0
coloring_books_left = 12.0

# the hypothesis refers to the number of coloring books left, which can be computed from the premise
# compute the number of coloring books left in the premise
coloring_books_left_premise = coloring_books_bought - coloring_books_given_away
if coloring_books_left_premise!= coloring_books_left:
    # check if the number of coloring books left in the hypothesis contradicts the number of coloring books left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
