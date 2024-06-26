ys_girls = 28.0
ys_boys = 35.0
total_children = 61.0

# the hypothesis refers to the total number of children, which is also mentioned in the premise
# compute the total number of children in the premise
total_children_premise = ys_girls + ys_boys
if total_children_premise!= total_children:
    # check if the total number of children in the hypothesis contradicts the total number of children in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values
    # we can infer entailment
    label = "entailment"

print(label)
