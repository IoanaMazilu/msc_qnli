students_cars_premise = 35
students_cars_hypothesis = 25

# the hypothesis refers to the percentage of students with cars mentioned in the premise
if students_cars_hypothesis >= students_cars_premise:
    # check if the 'students_cars_hypothesis' contradicts the estimate of less than 'students_cars_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
