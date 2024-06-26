shoes_premise = 27
more_shoes_hypothesis = 27

# the hypothesis refers to the number of shoes Marcella has, also mentioned in the premise
if shoes_premise <= more_shoes_hypothesis:
    # check if the estimate of'more_shoes_hypothesis' contradicts the number of shoes in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
