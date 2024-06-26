premise_ramesh = 60
premise_sushil = 25
hypothesis_ramesh = 20
hypothesis_sushil = 25

# the hypothesis refers to the number of days it takes to finish a work for both Ramesh and Sushil
if hypothesis_ramesh <= premise_ramesh and hypothesis_sushil <= premise_sushil:
    # check if the hypothesis values contradict the premise estimates
    label = "contradiction"
elif hypothesis_ramesh == premise_ramesh and hypothesis_sushil == premise_sushil:
    # check if the hypothesis values are consistent with the premise estimates
    label = "neutral"
else:
    # the hypothesis values are not consistent with the premise estimates, but can be entailed from the premise
    label = "entailment"

print(label)
