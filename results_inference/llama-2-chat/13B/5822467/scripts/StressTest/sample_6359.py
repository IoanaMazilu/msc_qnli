nice_premise = "since you're nice"
nice_hypothesis = "more than 5 baseball cards"
baseball_cards_premise = 5

# the hypothesis refers to the number of baseball cards given to John
if nice_hypothesis <= baseball_cards_premise:
    # check if the hypothesis value contradicts the number of baseball cards in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of baseball cards given to John
    # any number of baseball cards greater than 'baseball_cards_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
