girls_premise = 28.0
boys_premise = 35.0
total_children_hypothesis = 61.0

# the hypothesis refers to the total number of children, which is also referenced in the premise
if total_children_hypothesis == (girls_premise + boys_premise):
    # check if the total number of children in the hypothesis matches the total number of children from the premise
    label = "entailment"
elif girls_premise!= 28.0 or boys_premise!= 35.0:
    # check if the number of girls or boys in the hypothesis contradicts the number of girls or boys from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
