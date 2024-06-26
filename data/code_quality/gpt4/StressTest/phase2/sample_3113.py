books_bought_premise = 27
books_bought_hypothesis = 27

# the hypothesis refers to the number of books bought by Rahim, as mentioned in the premise
if books_bought_hypothesis >= books_bought_premise:
    # check if the hypothesis value contradicts the premise, which states that Rahim bought exactly 'books_bought_premise' books
    label = "contradiction"
else:
    # the premise gives an exact number of books bought
    # any number of books less than 'books_bought_premise' contradicts the premise
    label = "contradiction"

print(label)
