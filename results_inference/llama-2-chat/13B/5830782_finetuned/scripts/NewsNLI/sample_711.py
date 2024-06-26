money_stolen_premise = 45000
money_stolen_hypothesis = 45000

# the hypothesis mentions the amount of money allegedly stolen by Wheeler, which is also mentioned in the premise
if money_stolen_hypothesis!= money_stolen_premise:
    # check if the amount of money stolen in the hypothesis contradicts the amount of money stolen reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
