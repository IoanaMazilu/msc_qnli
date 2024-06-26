science_students_premise = 200
science_students_hypothesis = 200
science_students_locals_percentage_premise = 50
science_students_locals_percentage_hypothesis = 20

commerce_students_premise = 120
commerce_students_hypothesis = 120
commerce_students_locals_percentage_premise = 85
commerce_students_locals_percentage_hypothesis = 85

# the hypothesis refers to the percentage of local students from science and commerce streams
if (science_students_premise != science_students_hypothesis) or (commerce_students_premise != commerce_students_hypothesis):
    # check if the total number of science or commerce students in the hypothesis contradicts with the premise
    label = "contradiction"
elif (science_students_locals_percentage_hypothesis > science_students_locals_percentage_premise) or (commerce_students_locals_percentage_hypothesis != commerce_students_locals_percentage_premise):
    # check if the percentage of local science or commerce students in the hypothesis contradicts with the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
