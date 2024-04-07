# Premise: Clarissa is driving home from work, less than 610 miles away.
# Hypothesis: Clarissa is driving home from work, 110 miles away.
# Golden Label: neutral

distance_home_premise = 610
distance_home_hypothesis = 110

# the hypothesis talks about the distance to home from work, referenced also in the premise
if distance_home_hypothesis > distance_home_premise:
    # check if the hypothesis distance contradicts the estimate of less than 'distance_home_premise'
    label = "contradiction"
elif distance_home_hypothesis < distance_home_premise:
    # the hypothesis distance is less than the premise distance, but the premise does not give an exact distance
    # so the hypothesis can't be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis distance matches exactly the premise distance, it would be an entailment
    label = "entailment"

print(label)

