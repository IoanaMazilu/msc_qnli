car_students_premise = 18
car_students_hypothesis = 58

# the hypothesis refers to the percentage of students at Morse with cars, also mentioned in the premise
if car_students_hypothesis!= car_students_premise:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
