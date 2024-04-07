# Premise: Dan’s car gets less than 52 miles per gallon.
# Hypothesis: Dan’s car gets 32 miles per gallon.
# Golden Label: neutral

mileage_premise = 52
mileage_hypothesis = 32

# the hypothesis mentions a specific mileage for Dan's car, which is also the subject of the premise
if mileage_hypothesis >= mileage_premise:
    # check if the mileage stated in the hypothesis contradicts the 'less than mileage_premise' estimate from the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for the mileage
    # any mileage less than 'mileage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

