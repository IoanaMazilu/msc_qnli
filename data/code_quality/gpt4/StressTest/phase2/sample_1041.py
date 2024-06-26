baseball_cards_premise = 6
baseball_cards_hypothesis = 4

# the hypothesis refers to the number of baseball cards given to John, also mentioned in the premise
if baseball_cards_premise <= baseball_cards_hypothesis:
    # check if the number of 'baseball_cards_hypothesis' contradicts the number of baseball cards given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
