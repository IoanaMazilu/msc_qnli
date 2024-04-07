# Premise: Since you're nice, you give John 7 baseball cards.
# Hypothesis: Since you're nice, you give John more than 5 baseball cards.
# Golden Label: entailment

baseball_cards_premise = 7
baseball_cards_hypothesis = 5

# the hypothesis refers to the number of baseball cards given to John mentioned in the premise
if baseball_cards_premise <= baseball_cards_hypothesis:
    # check if the estimate of 'baseball_cards_hypothesis' contradicts the number of baseball cards in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
