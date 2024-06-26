weight_premise = 50
weight_hypothesis = 10
percentage_premise = 50
percentage_hypothesis = 50

# the hypothesis refers to the weight and the percentage of weight compared to the sister
if weight_hypothesis >= weight_premise:
    # check if the weight in the hypothesis contradicts the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
