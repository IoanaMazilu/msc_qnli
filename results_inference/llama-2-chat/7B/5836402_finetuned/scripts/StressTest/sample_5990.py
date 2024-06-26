mpg_premise = 32
mpg_hypothesis = 82

# the hypothesis refers to the car's fuel efficiency, which is also mentioned in the premise
if mpg_hypothesis!= mpg_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
