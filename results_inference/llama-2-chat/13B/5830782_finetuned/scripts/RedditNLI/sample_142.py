cost_premise = 1
cost_hypothesis = 1

# the hypothesis and premise mention the cost of the loan scandal at Wells Fargo
if cost_hypothesis!= cost_premise:
    # check if the cost in the hypothesis contradicts the cost in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
