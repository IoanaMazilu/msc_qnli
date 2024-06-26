returned_tshirts_premise = 5
returned_tshirts_hypothesis = 4

if returned_tshirts_hypothesis >= returned_tshirts_premise:
    # check if the number of returned t-shirts in the hypothesis contradicts the number of returned t-shirts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
