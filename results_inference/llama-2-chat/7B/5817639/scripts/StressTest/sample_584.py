books_bought_premise = 65
books_bought_hypothesis = float(hypothesis)

# the hypothesis talks about the number of books bought, referenced also in the premise
if books_bought_hypothesis > books_bought_premise:
    # check if the hypothesis value contradicts the estimate of 'books_bought_premise'
    label = "contradiction"
elif books_bought_hypothesis == books_bought_premise:
    # if the hypothesis value matches the estimate of 'books_bought_premise', we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is neither greater nor equal to the estimate of 'books_bought_premise', we cannot infer entailment or contradiction
    label = "neutral"

print(label)
