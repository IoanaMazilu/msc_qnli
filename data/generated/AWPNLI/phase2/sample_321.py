# Premise: There are 4.0 children in the classroom, each student will get 2.0 pencils.
# Hypothesis: The teacher will have to give out 3.0 pencils.
# Golden Label: contradiction

children_premise = 4.0
pencils_per_child_premise = 2.0
total_pencils_hypothesis = 3.0

# the hypothesis refers to the total number of pencils given out, which can be calculated from the premise
# compute the total number of pencils in the premise
total_pencils_premise = children_premise * pencils_per_child_premise
if total_pencils_hypothesis != total_pencils_premise:
    # check if the total number of pencils in the hypothesis contradicts the total number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

