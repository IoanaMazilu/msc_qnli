books_bought_premise = 65
books_bought_hypothesis = 65

# the hypothesis refers to the number of books bought by Rahim mentioned in the premise
if books_bought_hypothesis >= books_bought_premise:
    # check if the hypothesis value contradicts the exact number of books bought in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of books bought
    # any number of books less than 'books_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
