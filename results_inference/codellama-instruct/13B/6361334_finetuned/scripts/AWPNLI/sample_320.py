num_children_premise = 4.0
num_pencils_per_child_premise = 2.0
num_pencils_hypothesis = 8.0

# the hypothesis refers to the number of pencils that the teacher will have to give out, which is also mentioned in the premise
# compute the total number of pencils that will be given out based on the number of children and the number of pencils per child
total_pencils_premise = num_children_premise * num_pencils_per_child_premise
if total_pencils_hypothesis!= total_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
