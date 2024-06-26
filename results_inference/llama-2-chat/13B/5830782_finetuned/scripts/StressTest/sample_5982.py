students_car_premise = 25
students_car_hypothesis = 35

# the hypothesis refers to the percentage of students at Morse who have cars, as mentioned in the premise
if students_car_hypothesis <= students_car_premise:
    # check if the hypothesis percentage contradicts the premise percentage
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
