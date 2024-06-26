weight_premise = 40000
weight_hypothesis = 160000
sand_weight_premise = 85000
sand_weight_hypothesis = 85000

# the hypothesis mentions a longer slab of weathered crude and sand, which is not mentioned in the premise
if weight_hypothesis!= weight_premise:
    # check if the weight of the slab in the hypothesis contradicts the weight reported in the premise
    label = "contradiction"
elif sand_weight_hypothesis!= sand_weight_premise:
    # check if the weight of the sand in the hypothesis contradicts the weight of the sand in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
