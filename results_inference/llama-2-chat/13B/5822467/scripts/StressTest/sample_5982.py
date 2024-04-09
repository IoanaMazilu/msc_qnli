percentage_students_premise = 25
percentage_students_hypothesis = 35

# the hypothesis talks about the percentage of students with cars, referenced also in the premise
if percentage_students_hypothesis <= percentage_students_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_students_premise'
    label = "contradiction"
elif percentage_students_hypothesis > percentage_students_premise:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage less than or equal to 35% is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
