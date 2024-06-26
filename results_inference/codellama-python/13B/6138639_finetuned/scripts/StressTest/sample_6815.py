car_percentage_premise = 18
car_percentage_hypothesis = 58

# the hypothesis talks about the percentage of students with cars at Morse, referenced also in the premise
if car_percentage_hypothesis!= car_percentage_premise:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
