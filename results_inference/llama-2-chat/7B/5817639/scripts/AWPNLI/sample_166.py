girls_premise = 28.0
boys_premise = 35.0
total_children_premise = girls_premise + boys_premise
hypothesis_children = 63.0

# check if the number of children in the hypothesis contradicts the number of children in the premise
if hypothesis_children!= total_children_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
