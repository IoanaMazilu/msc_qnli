percentage_students_premise = 18
percentage_students_hypothesis = 48

# the hypothesis refers to the percentage of students with cars at Morse, mentioned in the premise
if percentage_students_hypothesis <= percentage_students_premise:
    # check if the estimate of 'percentage_students_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage of students with cars greater than 'percentage_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
