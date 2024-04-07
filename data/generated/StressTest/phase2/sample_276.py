# Premise: On the first day of her vacation, Louisa traveled 160 miles.
# Hypothesis: On the first day of her vacation, Louisa traveled less than 660 miles.
# Golden Label: entailment

miles_traveled_premise = 160
miles_traveled_hypothesis = 660

# the hypothesis refers to the miles traveled by Louisa on the first day of her vacation, which is also mentioned in the premise
if miles_traveled_premise >= miles_traveled_hypothesis:
    # check if the miles traveled in the premise contradicts the estimate of less than 'miles_traveled_hypothesis'
    label = "contradiction"
else:
    # if the miles_traveled_premise is below the estimate of the 'miles_traveled_hypothesis', we can infer entailment
    label = "entailment"

print(label)

