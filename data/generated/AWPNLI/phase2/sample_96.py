# Premise: Each child has 3.0 oranges, and there are 4.0 children.
# Hypothesis: 12.0 oranges are there in total.
# Golden Label: entailment

oranges_per_child_premise = 3.0
children_premise = 4.0
total_oranges_hypothesis = 12.0

# the hypothesis refers to the total number of oranges, which can be calculated from the premise
# compute the total number of oranges in the premise
total_oranges_premise = oranges_per_child_premise * children_premise
if total_oranges_hypothesis != total_oranges_premise:
    # check if the total number of oranges in the hypothesis contradicts the total number of oranges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

