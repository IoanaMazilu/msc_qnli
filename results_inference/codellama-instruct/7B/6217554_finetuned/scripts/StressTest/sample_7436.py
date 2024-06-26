total_premise = 90
total_hypothesis = 90
tax_premise = 0.2
tax_hypothesis = 0.2
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the total cost, tax rate and rebate mentioned in the premise
if total_hypothesis >= total_premise:
    # check if the total cost in the hypothesis contradicts the total cost reported in the premise
    label = "contradiction"
elif tax_hypothesis!= tax_premise:
    # check if the tax rate in the hypothesis contradicts the tax rate reported in the premise
    label = "contradiction"
elif rebate_hypothesis!= rebate_premise:
    # check if the rebate in the hypothesis contradicts the rebate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
