car_students_premise = 18
car_students_hypothesis = 48

# the hypothesis refers to the percentage of students at Morse who have cars, as mentioned in the premise
if car_students_hypothesis <= car_students_premise:
    # check if the estimate of 'car_students_hypothesis' contradicts the percentage of students at Morse who have cars in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
