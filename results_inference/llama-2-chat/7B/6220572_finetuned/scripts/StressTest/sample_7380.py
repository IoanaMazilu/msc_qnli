books_bought_premise = 6
books_bought_hypothesis = 60

# the hypothesis refers to the number of books bought and their average price mentioned in the premise
if books_bought_hypothesis <= books_bought_premise:
    # check if the estimate of 'books_bought_hypothesis' contradicts the number of books bought in the premise
    label = "contradiction"
else:
    # any average price greater than 'books_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
