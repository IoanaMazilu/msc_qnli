percentage_students_cars_premise = 0.18
percentage_students_cars_hypothesis = 0.58

# the hypothesis refers to the percentage of students with cars mentioned in the premise
if percentage_students_cars_hypothesis!= percentage_students_cars_premise:
    # check if the estimate of 'percentage_students_cars_hypothesis' contradicts the percentage of students with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
