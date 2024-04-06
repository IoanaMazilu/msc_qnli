# Premise: USGS originally put the magnitude at 4.1 before revising it to 3.8.
# Hypothesis: USGS revises magnitude down from 4.1 to 3.8.
# Golden Label: entailment

original_magnitude_premise = 4.1
revised_magnitude_premise = 3.8

original_magnitude_hypothesis = 4.1
revised_magnitude_hypothesis = 3.8

# the hypothesis mentions the original and revised magnitudes, which are also mentioned in the premise
if original_magnitude_hypothesis != original_magnitude_premise:
    # check if the original magnitude in the hypothesis contradicts the original magnitude reported in the premise
    label = "contradiction"
elif revised_magnitude_hypothesis != revised_magnitude_premise:
    # check if the revised magnitude from the hypothesis contradicts the revised magnitude in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

