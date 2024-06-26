miles_traveled_premise = 240
miles_traveled_hypothesis = 340

# the hypothesis refers to the number of miles Louisa traveled on the first day of her vacation, which is also mentioned in the premise
if miles_traveled_hypothesis!= miles_traveled_premise:
    # check if the number of miles traveled in the hypothesis contradicts the number of miles traveled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
