traveled_miles_premise = 200
traveled_miles_hypothesis = 300

# the hypothesis refers to the number of miles traveled by Louisa on the first day of her vacation, mentioned in the premise
if traveled_miles_hypothesis >= traveled_miles_premise:
    # check if the estimate of 'traveled_miles_hypothesis' contradicts the number of miles traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
