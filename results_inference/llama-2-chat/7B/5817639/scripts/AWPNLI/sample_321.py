children_premise = 4.0
pencils_per_student_premise = 2.0
total_pencils_premise = children_premise * pencils_per_student_premise
hypothesis_pencils = 3.0

# check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
if hypothesis_pencils!= total_pencils_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
