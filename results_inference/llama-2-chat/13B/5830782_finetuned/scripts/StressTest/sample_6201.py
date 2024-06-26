miles_traveled_premise = 200
miles_traveled_hypothesis = 300

# the hypothesis refers to the distance traveled by Louisa, which is also mentioned in the premise
if miles_traveled_premise > miles_traveled_hypothesis:
    # check if the distance traveled by Louisa in the premise contradicts the estimate of less than'miles_traveled_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
