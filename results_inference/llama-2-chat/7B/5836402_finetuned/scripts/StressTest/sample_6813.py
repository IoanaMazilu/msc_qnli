car_percentage_premise = 0.18
car_percentage_hypothesis = 0.48

# the hypothesis refers to the percentage of students with cars mentioned in the premise
if car_percentage_premise >= car_percentage_hypothesis:
    # check if the estimate of 'car_percentage_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
elif car_percentage_premise <= 0:
    # check if the percentage of students with cars in the premise is less than 'car_percentage_hypothesis'
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
