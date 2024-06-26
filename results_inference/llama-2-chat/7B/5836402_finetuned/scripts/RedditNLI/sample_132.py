wage_premise = 15
wage_hypothesis = 15

# the hypothesis and premise mention the minimum wage in California
if wage_hypothesis!= wage_premise:
    # check if the minimum wage in the hypothesis contradicts the minimum wage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
