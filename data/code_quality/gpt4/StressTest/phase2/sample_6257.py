discount_premise = 20
discount_hypothesis = 50
saved_money_premise = 4
saved_money_hypothesis = 4

# the hypothesis is referring to the discount and the saved money per person mentioned in the premise
if discount_premise != discount_hypothesis:
    # check if the discount percentage in the hypothesis contradicts the discount reported in the premise
    label = "contradiction"
elif saved_money_premise != saved_money_hypothesis:
    # check if the saved money per person in the hypothesis contradicts the saved money per person reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
