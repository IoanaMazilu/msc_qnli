total_commute_premise = 55
total_commute_hypothesis = 15

# the hypothesis talks about the difference in commute time between walking and train, referenced also in the premise
if total_commute_hypothesis <= total_commute_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_commute_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in commute time
    # any difference greater than 'total_commute_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
