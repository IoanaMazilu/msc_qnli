car_ratio_premise = 0.2
car_ratio_hypothesis = 0.5

# the hypothesis refers to the car ratio at Morse, which is also mentioned in the premise
if car_ratio_hypothesis >= car_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'car_ratio_premise'
    label = "contradiction"
elif car_ratio_hypothesis < car_ratio_premise:
    # if the hypothesis value is less than the premise estimate, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise estimate, we cannot make a conclusion
    label = "neutral"

print(label)
