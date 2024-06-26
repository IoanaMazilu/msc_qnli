books_bought_premise = 50
books_bought_hypothesis = 40

# the hypothesis talks about the number of books Rahim bought, referenced also in the premise
if books_bought_premise <= books_bought_hypothesis:
    # check if the number of books in the hypothesis contradicts the number of books mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
