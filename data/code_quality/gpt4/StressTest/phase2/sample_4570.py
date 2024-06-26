# we use the ratio values as numerical entities (for example 5:5 -> 5/5=1)
kunal_sagar_ratio_premise = 5/5
kunal_sagar_ratio_hypothesis = 6/5

# the hypothesis talks about the ratio of ages between Kunal and Sagar, which is also mentioned in the premise
if kunal_sagar_ratio_hypothesis <= kunal_sagar_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'kunal_sagar_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio greater than 'kunal_sagar_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
