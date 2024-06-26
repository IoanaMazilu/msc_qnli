mpg_premise = 32
mpg_hypothesis = 62

# the hypothesis refers to the mileage of Dan's car mentioned in the premise
if mpg_premise >= mpg_hypothesis:
    # check if the estimate of'mpg_hypothesis' contradicts the mileage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
