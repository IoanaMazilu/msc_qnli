# Premise: There were 27.0 boys and 35.0 girls on the playground at recess.
# Hypothesis: 66.0 children were on the playground at recess.
# Golden Label: contradiction

boys_premise = 27.0
girls_premise = 35.0
total_children_hypothesis = 66.0

# the hypothesis implies the total number of children, which can be inferred from the premise
# compute the total number of children in the premise
total_children_premise = boys_premise + girls_premise
if total_children_hypothesis != total_children_premise:
    # check if the total number of children in the hypothesis contradicts the total number of children from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
