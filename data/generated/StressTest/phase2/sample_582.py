# Premise: Rahim bought 65 books for Rs.
# Hypothesis: Rahim bought more than 25 books for Rs.
# Golden Label: entailment

books_bought_premise = 65
books_bought_hypothesis = 25

# the hypothesis talks about the number of books bought by Rahim, referenced also in the premise
if books_bought_premise <= books_bought_hypothesis:
    # check if the hypothesis value contradicts the exact number of 'books_bought_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of books bought
    # any number of books less than 'books_bought_premise' is consistent with the premise, hence we can infer entailment
    label = "entailment"

print(label)

