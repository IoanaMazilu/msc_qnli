children_premise = 4.0
pencils_per_child_premise = 2.0
pencils_hypothesis = 3.0

# the hypothesis refers to the number of pencils that the teacher will have to give out
# compute the total number of pencils that the teacher will have to give out
total_pencils_hypothesis = children_premise * pencils_per_child_premise
if total_pencils_hypothesis!= pencils_hypothesis:
    # check if the number of pencils in the hypothesis contradicts the number of pencils that the teacher will have to give out
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
