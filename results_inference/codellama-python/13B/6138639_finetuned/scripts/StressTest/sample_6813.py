students_with_cars_premise = 18
students_with_cars_hypothesis = 48

# the hypothesis refers to the percentage of students with cars at Morse, mentioned in the premise
if students_with_cars_premise >= students_with_cars_hypothesis:
    # check if the estimate of'students_with_cars_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
