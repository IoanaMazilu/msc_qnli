mpg_premise = 32
mpg_hypothesis = 82

# the hypothesis refers to the mileage of Dan's car mentioned in the premise
if mpg_hypothesis!= mpg_premise:
    # check if the mileage in the hypothesis contradicts the mileage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
