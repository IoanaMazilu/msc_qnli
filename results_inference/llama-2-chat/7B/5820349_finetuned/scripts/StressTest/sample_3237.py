car_students_premise = 20
car_students_hypothesis = 50

# the hypothesis refers to the percentage of students with cars at Morse mentioned in the premise
if car_students_premise >= car_students_hypothesis:
    # check if the estimate of 'car_students_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
