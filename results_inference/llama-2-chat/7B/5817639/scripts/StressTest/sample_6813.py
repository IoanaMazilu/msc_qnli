student_car_premise = 0.18
student_car_hypothesis = 0.48

# the hypothesis talks about the percentage of students with cars at Morse, which is also referred to in the premise
if student_car_hypothesis <= student_car_premise:
    # check if the hypothesis value contradicts the estimate of'student_car_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of students with cars, which can be fully entailed from the premise
    label = "entailment"

print(label)
