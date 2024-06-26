cotton_percentage_premise = 0.04
cotton_percentage_hypothesis = 0.04

# the hypothesis refers to the cotton percentage in luxury lingerie, which is also referenced in the premise
if cotton_percentage_hypothesis != cotton_percentage_premise:
    # check if the cotton percentage in the hypothesis contradicts the cotton percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
