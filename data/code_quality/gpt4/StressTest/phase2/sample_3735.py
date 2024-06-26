miles_per_gallon_premise = 32
miles_per_gallon_hypothesis = 52

# the hypothesis refers to the mileage of Dan's car mentioned in the premise
if miles_per_gallon_premise >= miles_per_gallon_hypothesis:
    # check if the mileage in the premise contradicts the estimate of less than 'miles_per_gallon_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact mileage for Dan's car
    # any mileage less than 'miles_per_gallon_hypothesis' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
