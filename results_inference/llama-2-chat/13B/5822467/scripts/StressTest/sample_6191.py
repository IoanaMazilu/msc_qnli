lexi_days_premise = 30
lexi_days_hypothesis = 45
lexi_pay_premise = 125

# the hypothesis refers to the number of days Lexi needed to save for the vacation
if lexi_days_hypothesis <= lexi_days_premise:
    # check if the hypothesis value contradicts the estimate of 'lexi_days_premise'
    label = "contradiction"
elif lexi_pay_premise!= lexi_days_hypothesis * 125:
    # check if the hypothesis value contradicts the amount of money Lexi needed to save for the vacation
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
