traveled_miles_premise = 300
traveled_miles_hypothesis = 200

if traveled_miles_hypothesis >= traveled_miles_premise:
    # check if the number of traveled miles in the hypothesis contradicts the estimate of less than 'traveled_miles_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of traveled miles
    # any number of traveled miles less than 'traveled_miles_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
