car_percentage_premise = 0.25
car_percentage_hypothesis = 0.85

# the hypothesis refers to the percentage of students with cars, which is also mentioned in the premise
if car_percentage_premise!= car_percentage_hypothesis:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # if the percentage of students with cars in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
