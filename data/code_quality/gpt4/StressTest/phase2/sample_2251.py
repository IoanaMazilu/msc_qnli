miles_per_gallon_premise = 72
miles_per_gallon_hypothesis = 32

# the hypothesis talks about the mileage of Dan's car, referenced also in the premise
if miles_per_gallon_hypothesis >= miles_per_gallon_premise:
    # check if the hypothesis value contradicts the estimate of less than 'miles_per_gallon_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the mileage per gallon
    # any mileage less than 'miles_per_gallon_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
