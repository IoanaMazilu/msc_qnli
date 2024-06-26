money_to_john_premise = 95
money_to_john_hypothesis = 35

# the hypothesis talks about the amount of money wanted to be given to John, which is also referred to in the premise
if money_to_john_premise <= money_to_john_hypothesis:
    # check if the hypothesis money value contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
