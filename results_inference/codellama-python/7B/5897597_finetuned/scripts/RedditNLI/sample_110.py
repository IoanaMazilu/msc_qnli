sales_increase_premise = 1.5
sales_increase_hypothesis = 1.5

# the hypothesis and premise mention the percentage increase in pending sales of homes in March
if sales_increase_hypothesis!= sales_increase_premise:
    # check if the percentage increase in the hypothesis contradicts the percentage increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
