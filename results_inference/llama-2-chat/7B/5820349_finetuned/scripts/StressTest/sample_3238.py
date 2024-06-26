car_students_premise = 50
car_students_hypothesis = 20

# the hypothesis refers to the percentage of students at Morse with cars, also mentioned in the premise
if car_students_hypothesis >= car_students_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'car_students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage less than 'car_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
