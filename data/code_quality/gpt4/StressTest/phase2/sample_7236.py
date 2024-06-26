miles_traveled_premise = 240
miles_traveled_hypothesis = 440

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, mentioned in the premise
if miles_traveled_hypothesis <= miles_traveled_premise:
    # check if the estimate of 'miles_traveled_hypothesis' contradicts the exact distance mentioned in the premise
    label = "contradiction"
elif miles_traveled_premise >= miles_traveled_hypothesis:
    # check if the distance traveled in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
