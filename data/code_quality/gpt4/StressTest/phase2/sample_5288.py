grapes_purchased_premise = 8
grapes_purchased_hypothesis = 6
rate_grapes_premise = 70
rate_grapes_hypothesis = 70
mangoes_purchased_premise = 9
mangoes_purchased_hypothesis = 9
rate_mangoes_premise = 55
rate_mangoes_hypothesis = 55

# the hypothesis refers to the quantities and rates of purchased grapes and mangoes mentioned in the premise
if rate_grapes_premise != rate_grapes_hypothesis or rate_mangoes_premise != rate_mangoes_hypothesis:
    # check if the rates of grapes or mangoes in the hypothesis contradict the rates in the premise
    label = "contradiction"
elif grapes_purchased_premise < grapes_purchased_hypothesis or mangoes_purchased_premise != mangoes_purchased_hypothesis:
    # check if the quantities of purchased grapes or mangoes in the hypothesis contradict the quantities in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
