# Premise: During the first two weeks of April, the total rainfall in Springdale was more than 10 inches.
# Hypothesis: During the first two weeks of April, the total rainfall in Springdale was 30 inches.
# Golden Label: neutral

rainfall_premise = 10
rainfall_hypothesis = 30

# the hypothesis talks about the total rainfall in Springdale in the first two weeks of April, referenced also in the premise
if rainfall_hypothesis <= rainfall_premise:
    # check if the hypothesis value contradicts the estimate of more than 'rainfall_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total rainfall
    # any amount of rainfall greater than 'rainfall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

