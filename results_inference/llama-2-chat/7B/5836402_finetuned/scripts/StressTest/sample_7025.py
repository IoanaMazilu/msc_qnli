speed_premise = 30
speed_hypothesis = 10

# the hypothesis refers to the speed at which Cara drives from City A to City B mentioned in the premise
if speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
