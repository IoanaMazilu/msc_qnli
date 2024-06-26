cards_given_premise = 5
cards_given_hypothesis = 5

# the hypothesis refers to the number of baseball cards given to John mentioned in the premise
if cards_given_hypothesis <= cards_given_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact number of cards given
    # any number of cards greater than 'cards_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
