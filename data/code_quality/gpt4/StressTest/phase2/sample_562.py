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
