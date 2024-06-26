john_premise = 4800
john_hypothesis = 3800

# the hypothesis refers to the amount of money John has, which is also mentioned in the premise
if john_premise <= john_hypothesis:
    # check if the estimate of 'john_hypothesis' contradicts the amount of money John has in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
