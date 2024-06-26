children_premise = 4.0
pencils_per_student_premise = 2.0
total_pencils_hypothesis = 3.0

# the hypothesis talks about the number of pencils to be given out, which is also referenced in the premise
# compute the total number of pencils to be given out in the premise
total_pencils_premise = children_premise * pencils_per_student_premise
if total_pencils_hypothesis!= total_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
