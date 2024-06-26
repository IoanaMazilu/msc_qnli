percentage_students_premise = 18
percentage_students_hypothesis = 48

# the hypothesis refers to the percentage of students with cars mentioned in the premise
if percentage_students_hypothesis <= percentage_students_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage less than 'percentage_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
