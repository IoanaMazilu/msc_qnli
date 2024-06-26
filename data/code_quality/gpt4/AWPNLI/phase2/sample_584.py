boys_premise = 40.0
girls_premise = 117
total_children_hypothesis = 157.0

# the hypothesis refers to the total number of children, which can be computed as the sum of boys and girls from the premise
# compute the total number of children in the premise
total_children_premise = boys_premise + girls_premise
if total_children_hypothesis != total_children_premise:
    # check if the total number of children in the hypothesis contradicts the total number of children from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
