books_bought_premise = 65
books_bought_hypothesis = 65

# the hypothesis refers to the number of books bought in the premise
if books_bought_hypothesis <= books_bought_premise:
    # check if the estimate of 'books_bought_hypothesis' contradicts the number of books bought in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of books bought
    # any number of books bought greater than 'books_bought_premise' is consistent with the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
