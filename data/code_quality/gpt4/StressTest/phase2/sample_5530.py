debentures_premise = 80000
debentures_hypothesis = 60000

# the hypothesis refers to the amount of debentures bought by Jaclyn mentioned in the premise
if debentures_hypothesis >= debentures_premise:
    # check if the amount of 'debentures_hypothesis' contradicts the estimate of less than 'debentures_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of debentures
    # any amount of debentures less than 'debentures_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
