money_given_premise = 30
money_given_hypothesis = 20

# the hypothesis refers to the amount of money given by Cindy's mother, which is also mentioned in the premise
if money_given_premise <= money_given_hypothesis:
    # check if the amount given in the hypothesis contradicts the amount given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
