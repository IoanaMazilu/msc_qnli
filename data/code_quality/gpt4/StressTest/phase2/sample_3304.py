miles_per_gallon_premise = 62
miles_per_gallon_hypothesis = 32

# the hypothesis defines a specific value for the miles per gallon of Dan's car, which is also the subject of the premise
if miles_per_gallon_hypothesis >= miles_per_gallon_premise:
    # check if the hypothesis value contradicts the estimate of less than 'miles_per_gallon_premise'
    label = "contradiction"
else:
    # any value less than 'miles_per_gallon_premise' is consistent with the premise, therefore we can infer entailment
    label = "entailment"

print(label)
