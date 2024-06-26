books_bought_premise = 15
books_bought_hypothesis = 75

# the hypothesis talks about the number of books bought by Alka, referenced also in the premise
if books_bought_hypothesis < books_bought_premise:
    # check if the hypothesis value contradicts the exact number of 'books_bought_premise'
    label = "contradiction"
elif books_bought_hypothesis == books_bought_premise:
    # check if the hypothesis value is the same as the premise's
    label = "entailment"
else:
    # any number of books less than 'books_bought_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
