subject_grades_premise = [45, 67, 76, 82, 85]
subject_grades_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis talks about the grades obtained by Reeya in different subjects, same as the premise
if sum(subject_grades_hypothesis) <= sum(subject_grades_premise):
    # check if the sum of the hypothesis grades contradicts the sum of the premise grades
    label = "contradiction"
else:
    # the premise gives an estimate for the average grades, but the hypothesis provides a more specific estimate
    label = "entailment"

print(label)
