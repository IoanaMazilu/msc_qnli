girls_premise = 28
boys_premise = 35
children_hypothesis = 63

# the hypothesis refers to the number of children, which are also mentioned in the premise
# compute the total number of children in the premise
total_children_premise = girls_premise + boys_premise
if children_hypothesis!= total_children_premise:
    # check if the number of children in the hypothesis contradicts the number of children from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
