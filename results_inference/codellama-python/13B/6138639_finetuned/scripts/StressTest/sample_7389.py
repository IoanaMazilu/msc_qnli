rosy_efficiency_premise = 10
mary_efficiency_premise = 0
rosy_efficiency_hypothesis = 30

# the hypothesis talks about the efficiency of Rosy compared to Mary, referenced also in the premise
if rosy_efficiency_premise > rosy_efficiency_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'rosy_efficiency_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the efficiency of Rosy
    # any efficiency of Rosy less than 'rosy_efficiency_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
