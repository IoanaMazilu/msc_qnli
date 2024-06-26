shoes_premise = 27
shoes_hypothesis = 17

# the hypothesis refers to the number of pairs of shoes Marcella has, mentioned in the premise
if shoes_premise <= shoes_hypothesis:
    # check if the number of pairs of shoes in the premise contradicts the estimate of more than'shoes_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
