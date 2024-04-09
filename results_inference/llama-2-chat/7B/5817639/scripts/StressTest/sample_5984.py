percentage_students_premise = 0.25
percentage_students_hypothesis = 0.85

# the hypothesis talks about a different percentage of students having cars than the premise
if percentage_students_hypothesis >= percentage_students_premise:
    # check if the estimate of 'percentage_students_hypothesis' contradicts the percentage of students in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students,
    # any percentage greater than 'percentage_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
