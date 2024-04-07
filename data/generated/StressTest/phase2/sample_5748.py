# Premise: During the first two weeks of April, the total rainfall in Springdale was 30 inches.
# Hypothesis: During the first two weeks of April, the total rainfall in Springdale was more than 10 inches.
# Golden Label: entailment

rainfall_premise = 30
rainfall_hypothesis = 10

# the hypothesis talks about the total rainfall in the first two weeks of April, also mentioned in the premise
if rainfall_premise < rainfall_hypothesis:
    # check if the hypothesis value contradicts the 'rainfall_premise'
    label = "contradiction"
elif rainfall_premise == rainfall_hypothesis:
    # check if the hypothesis value equals the 'rainfall_premise'
    label = "neutral"
else:
    # if the 'rainfall_premise' is more than 'rainfall_hypothesis', we can infer entailment
    label = "entailment"

print(label)

