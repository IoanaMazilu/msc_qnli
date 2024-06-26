yhat_premise = 32
yhat_hypothesis = 82

# the hypothesis refers to the car's mileage, which is also mentioned in the premise
if yhat_hypothesis!= yhat_premise:
    # check if the mileage in the hypothesis contradicts the mileage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
