baseball_cards_premise = 5
baseball_cards_hypothesis = 5

# the hypothesis refers to the number of baseball cards given to John
if baseball_cards_hypothesis <= baseball_cards_premise:
    # check if the estimate of 'baseball_cards_hypothesis' contradicts the number of baseball cards given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of baseball cards given
    # any number of baseball cards greater than 'baseball_cards_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
