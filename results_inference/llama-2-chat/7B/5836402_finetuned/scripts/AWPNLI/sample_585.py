boys_premise = 40.0
girls_premise = 117
total_children_hypothesis = 159.0

# the hypothesis refers to the total number of children, which are also mentioned in the premise
# compute the total number of children in the premise
total_children_premise = boys_premise + girls_premise
if total_children_hypothesis!= total_children_premise:
    # check if the number of children in the hypothesis contradicts the number of children from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
