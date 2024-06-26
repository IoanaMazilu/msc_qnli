oranges_premise = 4.0
children_premise = 3.0
oranges_per_child_hypothesis = 6.0

# the hypothesis refers to the number of oranges per child, which is also mentioned in the premise
# compute the number of oranges per child in the premise
oranges_per_child_premise = oranges_premise / children_premise
if oranges_per_child_hypothesis != oranges_per_child_premise:
    # check if the number of oranges per child in the hypothesis contradicts the number of oranges per child from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
