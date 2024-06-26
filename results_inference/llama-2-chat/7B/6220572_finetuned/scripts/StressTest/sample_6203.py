miles_traveled_premise = 200
miles_traveled_hypothesis = 200

# the hypothesis refers to the number of miles Louisa traveled on the first day of her vacation, as mentioned in the premise
if miles_traveled_hypothesis <= miles_traveled_premise:
    # check if the hypothesis value contradicts the number of miles Louisa traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
