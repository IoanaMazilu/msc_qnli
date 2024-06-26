car_percentage_premise = 50
car_percentage_hypothesis = 20

# the hypothesis refers to the percentage of students with cars, which is also mentioned in the premise
if car_percentage_premise <= car_percentage_hypothesis:
    # check if the estimate of 'car_percentage_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
elif car_percentage_hypothesis > car_percentage_premise:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage of students with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
