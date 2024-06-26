car_students_premise = 15
car_students_hypothesis = 35

# the hypothesis refers to the percentage of students with cars at Morse, as does the premise
if car_students_hypothesis < car_students_premise:
    # check if the hypothetical percentage is less than the percentage in the premise
    label = "contradiction"
elif car_students_hypothesis > car_students_premise:
    # the premise gives only an estimate for the percentage of students
    # any percentage less than 'car_students_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothetical percentage is equal to the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
