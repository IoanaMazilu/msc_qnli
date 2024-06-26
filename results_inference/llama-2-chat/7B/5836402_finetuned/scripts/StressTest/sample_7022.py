car_percentage_premise = 0.2
car_percentage_hypothesis = 0.5

# the hypothesis refers to the percentage of students with cars, mentioned in the premise
if car_percentage_hypothesis <= car_percentage_premise:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage of students with cars in the premise
    label = "contradiction"
elif car_percentage_hypothesis > car_percentage_premise:
    # if the percentage of students with cars in the hypothesis is greater than the percentage in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but the percentage of students with cars is less than the premise, we cannot infer entailment
    label = "neutral"

print(label)
