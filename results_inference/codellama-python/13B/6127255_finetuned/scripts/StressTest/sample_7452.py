T_premise = 105
T_hypothesis = 4/9 * (K-32)

# the hypothesis refers to the same situation as the premise, but with a different formula for T
if T_premise <= T_hypothesis:
    # check if the value of 'T_hypothesis' contradicts the value of T in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
