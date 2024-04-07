# Premise: Six years ago, the ratio of ages of Kunal and Sagar was more than 1:5.
# Hypothesis: Six years ago, the ratio of ages of Kunal and Sagar was 6:5.
# Golden Label: neutral

kunal_sagar_ratio_premise = 1/5
kunal_sagar_ratio_hypothesis = 6/5

# the hypothesis talks about the ratio of ages of Kunal and Sagar six years ago, which is also mentioned in the premise
if kunal_sagar_ratio_hypothesis <= kunal_sagar_ratio_premise:
    # check if the hypothesis value contradicts the premise which states the ratio was more than 'kunal_sagar_ratio_premise'
    label = "contradiction"
else:
    # the premise only gives a lower bound for the ratio of ages
    # any ratio greater than 'kunal_sagar_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

