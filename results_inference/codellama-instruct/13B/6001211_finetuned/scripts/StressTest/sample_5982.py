car_students_premise = 25
car_students_hypothesis = 35

# the hypothesis refers to the percentage of students at Morse who have cars, mentioned in the premise
if car_students_hypothesis <= car_students_premise:
    # check if the estimate of 'car_students_hypothesis' contradicts the percentage of car students in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
