percentage_students_premise = 0.2
percentage_students_hypothesis = 0.5

# the hypothesis talks about the percentage of students with cars, which is also referred to in the premise
if percentage_students_hypothesis <= percentage_students_premise:
    # check if the hypothesis value contradicts the estimate of 'percentage_students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage of students with cars less than 'percentage_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)