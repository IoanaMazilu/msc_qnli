coloring_books_bought = 48.0
coloring_books_given_away = 34.0 + 3.0
coloring_books_left = coloring_books_bought - coloring_books_given_away

# the hypothesis refers to the number of coloring books left
if coloring_books_left!= 12.0:
    # check if the number of coloring books left in the hypothesis contradicts the number of coloring books left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and calculations match the premise values, we can infer entailment
    label = "entailment"

print(label)
