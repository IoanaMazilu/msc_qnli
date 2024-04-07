# Premise: I want to give 95 $to John.
# Hypothesis: I want to give more than 85 $to John.
# Golden Label: entailment

money_to_give_premise = 95
money_to_give_hypothesis = 85

# the hypothesis refers to the amount of money to give to John, mentioned also in the premise
if money_to_give_hypothesis >= money_to_give_premise:
    # check if the estimate of 'money_to_give_hypothesis' contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

