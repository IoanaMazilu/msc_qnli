discount_premise = 20
discount_hypothesis = 30
dollar_savings_premise = 4
dollar_savings_hypothesis = 4

# the hypothesis refers to the discount percentage and the savings in dollars reported in the premise
if discount_hypothesis <= discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount percentage in the premise
    label = "contradiction"
elif dollar_savings_hypothesis!= dollar_savings_premise:
    # check if the savings in dollars in the hypothesis contradicts the savings in dollars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
