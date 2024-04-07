# Premise: If less than 50% of all the students at Morse have cars, how many students are in the three lower grades?
# Hypothesis: If 20% of all the students at Morse have cars, how many students are in the three lower grades?
# Golden Label: neutral

student_car_ownership_premise = 50
student_car_ownership_hypothesis = 20

# the hypothesis refers to the student car ownership mentioned in the premise
if student_car_ownership_hypothesis >= student_car_ownership_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'student_car_ownership_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the student car ownership
    # any percentage of student car ownership less than 'student_car_ownership_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

