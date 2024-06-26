miles_traveled_premise = 240
miles_traveled_hypothesis = 440

# the hypothesis refers to the number of miles Louisa traveled on the first day of her vacation, also mentioned in the premise
if miles_traveled_premise >= miles_traveled_hypothesis:
    # check if the estimate of'miles_traveled_hypothesis' contradicts the number of miles traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
