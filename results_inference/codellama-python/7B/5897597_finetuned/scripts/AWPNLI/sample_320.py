children_premise = 4.0
pencils_per_child_premise = 2.0
pencils_hypothesis = 8.0

# the hypothesis refers to the total number of pencils that the teacher will have to give out, which is also mentioned in the premise
# compute the total number of pencils that the teacher will have to give out in the premise
total_pencils_premise = children_premise * pencils_per_child_premise
if pencils_hypothesis!= total_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)