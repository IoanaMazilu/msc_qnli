cards_given_premise = 4
cards_given_hypothesis = 6

# the hypothesis talks about the number of baseball cards given to John, referenced also in the premise
if cards_given_hypothesis <= cards_given_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cards_given_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of baseball cards
    # any number of cards greater than 'cards_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
