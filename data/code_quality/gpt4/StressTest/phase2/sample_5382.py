rain_premise = 20
rain_hypothesis = 40

# The hypothesis refers to the total rainfall in Springdale during the first two weeks of February, which is also mentioned in the premise
if rain_premise > rain_hypothesis:
    # Check if the rainfall reported in the premise contradicts the hypothesis that it was less than 'rain_hypothesis'
    label = "contradiction"
elif rain_premise == rain_hypothesis:
    # Even though the rain in the premise does not contradict the hypothesis, it cannot be explicitly entailed since the hypothesis suggests it could be less
    label = "neutral"
else:
    # The premise's rainfall is less than the 'rain_hypothesis' which does not contradict the hypothesis
    label = "entailment"

print(label)
