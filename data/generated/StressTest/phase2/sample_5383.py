# Premise: During the first two weeks of February, the total rainfall in Springdale was less than 40 inches.
# Hypothesis: During the first two weeks of February, the total rainfall in Springdale was 20 inches.
# Golden Label: neutral

rainfall_premise = 40
rainfall_hypothesis = 20

# the hypothesis talks about the total rainfall in the first two weeks of February mentioned in the premise
if rainfall_hypothesis >= rainfall_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rainfall_premise'
    label = "contradiction"
else:
    # any amount of rainfall less than 'rainfall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

