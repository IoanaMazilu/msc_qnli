# Premise: The ratio of Gomati’s and Rashmi’s ages is less than 4:5 respectively.
# Hypothesis: The ratio of Gomati’s and Rashmi’s ages is 3:5 respectively.
# Golden Label: neutral

gomati_rashmi_ratio_premise = 4/5
gomati_rashmi_ratio_hypothesis = 3/5

# the hypothesis talks about the ratio of Gomati's and Rashmi's ages, mentioned also in the premise
if gomati_rashmi_ratio_hypothesis > gomati_rashmi_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of less than 'gomati_rashmi_ratio_premise'
    label = "contradiction"
elif gomati_rashmi_ratio_hypothesis == gomati_rashmi_ratio_premise:
    # if the ratio in the hypothesis is exactly 'gomati_rashmi_ratio_premise', it contradicts the 'less than' condition in the premise
    label = "contradiction"
else:
    # the premise gives an upper limit for the ratio
    # any ratio lower than 'gomati_rashmi_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

