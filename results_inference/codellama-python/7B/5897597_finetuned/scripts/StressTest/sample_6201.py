miles_traveled_premise = 200
miles_traveled_hypothesis = 300

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, mentioned in the premise
if miles_traveled_premise >= miles_traveled_hypothesis:
    # check if the distance traveled in the premise contradicts the estimate of less than'miles_traveled_hypothesis'
    label = "contradiction"
else:
    # if the premise distance does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
