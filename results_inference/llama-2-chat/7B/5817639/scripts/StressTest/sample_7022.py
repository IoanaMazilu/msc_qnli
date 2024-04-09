students_car_premise = 20
students_car_hypothesis = 50

# the hypothesis talks about the percentage of students with cars, referenced also in the premise
if students_car_hypothesis >= students_car_premise:
    # check if the hypothesis value contradicts the estimate of'students_car_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of students with cars
    # any percentage of students with cars greater than'students_car_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
