num_children_premise = 4.0
num_pencils_per_child_premise = 2.0
num_pencils_teacher_hypothesis = 3.0

# the hypothesis refers to the number of pencils the teacher will have to give out, which is also mentioned in the premise
# compute the total number of pencils that will be given out in the premise
total_pencils_premise = num_children_premise * num_pencils_per_child_premise
if num_pencils_teacher_hypothesis > total_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
