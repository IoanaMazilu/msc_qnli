car_students_premise = 18
car_students_hypothesis = 58

# the hypothesis refers to the percentage of students at Morse who have cars
if car_students_premise!= car_students_hypothesis:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
