car_students_percentage_premise = 20
car_students_percentage_hypothesis = 50

# the hypothesis refers to the percentage of students at Morse who have cars, mentioned in the premise
if car_students_percentage_hypothesis < car_students_percentage_premise:
    # check if the percentage of students at Morse who have cars in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
