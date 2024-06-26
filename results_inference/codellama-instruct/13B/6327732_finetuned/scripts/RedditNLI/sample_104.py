percentage_premise = 50
percentage_hypothesis = 50

# the hypothesis and premise mention the percentage of the population that is owned by the richest 85 people
if percentage_hypothesis!= percentage_premise:
    # check if the estimated percentage of the population in the hypothesis contradicts the premise estimate of 50%
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the population
    # any estimate of the percentage in the hypothesis greater or equal to 'percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
