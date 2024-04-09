car_students_premise = 20
car_students_hypothesis = 50

# the hypothesis refers to the percentage of students at Morse who have cars, as mentioned in the premise
if car_students_premise!= car_students_hypothesis:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # if the percentage of students with cars in the hypothesis does not contradict the percentage of students with cars in the premise, we can infer entailment
    label = "entailment"

print(label)
