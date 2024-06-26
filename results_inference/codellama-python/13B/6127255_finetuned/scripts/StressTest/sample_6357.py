baseball_cards_given_premise = 5
baseball_cards_given_hypothesis = 2

# the hypothesis refers to the number of baseball cards given to John mentioned in the premise
if baseball_cards_given_premise <= baseball_cards_given_hypothesis:
    # check if the estimate of 'baseball_cards_given_hypothesis' contradicts the number of cards given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
