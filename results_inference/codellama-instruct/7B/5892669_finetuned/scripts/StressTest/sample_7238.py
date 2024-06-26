miles_traveled_premise = 240
miles_traveled_hypothesis = 340

# the hypothesis refers to the miles traveled by Louisa on the first day of her vacation, mentioned in the premise
if miles_traveled_hypothesis!= miles_traveled_premise:
    # check if the miles traveled in the hypothesis contradicts the miles traveled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
