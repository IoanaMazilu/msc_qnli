# Premise: If the agreed period of the debenture was less than 68 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Hypothesis: If the agreed period of the debenture was 18 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Golden Label: neutral

debenture_period_premise = 68
debenture_period_hypothesis = 18

# the hypothesis talks about the period of the debenture, also referenced in the premise
if debenture_period_hypothesis >= debenture_period_premise:
    # check if the hypothesis value contradicts the estimate of less than 'debenture_period_premise'
    label = "contradiction"
elif debenture_period_hypothesis < debenture_period_premise:
    # if the hypothesis value is less than the premise value, the premise entails the hypothesis
    label = "entailment"

print(label)

