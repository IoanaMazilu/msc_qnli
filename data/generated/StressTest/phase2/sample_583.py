# Premise: Rahim bought more than 25 books for Rs.
# Hypothesis: Rahim bought 65 books for Rs.
# Golden Label: neutral

books_bought_premise = 25
books_bought_hypothesis = 65

# the hypothesis talks about the number of books bought by Rahim, referenced also in the premise
if books_bought_hypothesis <= books_bought_premise:
    # check if the hypothesis value contradicts the estimate of more than 'books_bought_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of books
    # any number of books greater than 'books_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

