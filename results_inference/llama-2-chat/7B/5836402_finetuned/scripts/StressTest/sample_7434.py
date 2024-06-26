store_value_premise = 90
store_value_hypothesis = 70
tax_rate_premise = 20
tax_rate_hypothesis = 20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the value of Store Z, tax rate, and rebate mentioned in the premise
if store_value_hypothesis <= store_value_premise:
    # check if the hypothesis value contradicts the estimate of more than'store_value_premise'
    label = "contradiction"
elif tax_rate_hypothesis!= tax_rate_premise:
    # check if the tax rate in the hypothesis contradicts the tax rate in the premise
    label = "contradiction"
elif rebate_hypothesis!= rebate_premise:
    # check if the rebate in the hypothesis contradicts the rebate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
