boys_premise = 40.0
total_children_premise = 117.0
girls_hypothesis = 79.0

# the hypothesis refers to the number of girls, which is also indirectly referred to in the premise
# compute the number of girls in the premise
girls_premise = total_children_premise - boys_premise
if girls_hypothesis != girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
