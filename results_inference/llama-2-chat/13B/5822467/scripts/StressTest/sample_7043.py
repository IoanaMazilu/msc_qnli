anna_weight_premise = 100
susan_weight_premise = 110 - anna_weight_premise
hypothesis_susan_weight = 80 + anna_weight_premise
total_weight_premise = anna_weight_premise + susan_weight_premise

# the hypothesis refers to Susan's weight and the total weight of both Anna and Susan
if hypothesis_susan_weight > total_weight_premise:
    # check if the estimate of Susan's weight contradicts the total weight reported in the premise
    label = "contradiction"
elif susan_weight_premise!= hypothesis_susan_weight:
    # check if the estimate of Susan's weight contradicts the weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
