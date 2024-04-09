student_car_premise = 25
student_car_hypothesis = 35

# the hypothesis talks about the percentage of students with cars, referenced also in the premise
if student_car_hypothesis <= student_car_premise:
    # check if the hypothesis value contradicts the estimate of'student_car_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of students with cars
    # any percentage of students with cars greater than'student_car_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
