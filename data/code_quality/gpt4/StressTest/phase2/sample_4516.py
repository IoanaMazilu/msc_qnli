AB_premise = 60
EC_premise = 20
AB_hypothesis = 10
EC_hypothesis = 20

# the hypothesis refers to the values of AB and EC mentioned in the premise
if AB_hypothesis >= AB_premise:
    # check if the value of 'AB_hypothesis' contradicts the estimate of less than 'AB_premise'
    label = "contradiction"
elif EC_hypothesis != EC_premise:
    # check if the value of 'EC_hypothesis' contradicts the value of 'EC_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of AB
    # any value of AB less than 'AB_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
