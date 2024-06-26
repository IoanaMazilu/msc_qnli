car_percentage_premise = 0.18
car_percentage_hypothesis = 0.48

# the hypothesis refers to the percentage of students with cars mentioned in the premise
if car_percentage_hypothesis <= car_percentage_premise:
    # check if the estimate of 'car_percentage_hypothesis' contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
