miles_traveled_premise = 240
miles_traveled_hypothesis = 440

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, as mentioned in the premise
if miles_traveled_premise > miles_traveled_hypothesis:
    # check if the distance traveled in the premise contradicts the estimate of 'less than miles_traveled_hypothesis'
    label = "contradiction"
elif miles_traveled_premise == miles_traveled_hypothesis:
    # check if the distance traveled in the premise exactly equals the estimate of 'less than miles_traveled_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
