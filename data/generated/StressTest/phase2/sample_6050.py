# Premise: I want to give 95 $to John.
# Hypothesis: I want to give 55 $to John.
# Golden Label: contradiction

money_premise = 95
money_hypothesis = 55

# the hypothesis talks about the amount of money I want to give to John, which is also mentioned in the premise
if money_hypothesis > money_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif money_hypothesis < money_premise:
    # check if the amount in the hypothesis is less than the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

