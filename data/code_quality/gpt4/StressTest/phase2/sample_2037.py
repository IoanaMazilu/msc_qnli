money_donald_premise = 900
money_donald_hypothesis = 100

# the hypothesis refers to the amount of money Donald has, as mentioned in the premise
if money_donald_premise <= money_donald_hypothesis:
    # check if the estimate of 'money_donald_hypothesis' contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
