car_percentage_premise = 0.18
car_percentage_hypothesis = 0.58

# the hypothesis refers to the percentage of students with cars at Morse, which is also mentioned in the premise
if car_percentage_premise!= car_percentage_hypothesis:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
