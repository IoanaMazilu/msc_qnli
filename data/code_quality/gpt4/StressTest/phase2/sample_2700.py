shoes_premise = 26
shoes_hypothesis = 16

# the hypothesis refers to the number of shoes Marcella has, which is also mentioned in the premise
if shoes_premise <= shoes_hypothesis:
    # check if the number of shoes in the premise contradicts the estimate of more than 'shoes_hypothesis' 
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
