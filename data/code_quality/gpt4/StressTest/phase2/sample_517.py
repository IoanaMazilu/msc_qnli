discount_premise = 80
discount_hypothesis = 20
saved_money_premise = 4
saved_money_hypothesis = 4

# the hypothesis refers to the discount and the saved money mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the 'discount_hypothesis' contradicts the premise's discount value
    label = "contradiction"
elif saved_money_hypothesis != saved_money_premise:
    # check if the saved money in the hypothesis contradicts the saved money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
