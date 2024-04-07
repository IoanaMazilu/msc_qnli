# Premise: Sam, Suresh and Sanket run a race of less than 7400 meters.
# Hypothesis: Sam, Suresh and Sanket run a race of 1400 meters.
# Golden Label: neutral

race_length_premise = 7400
race_length_hypothesis = 1400

# the hypothesis mentions the exact length of the race also referenced in the premise
if race_length_hypothesis >= race_length_premise:
    # check if the hypothesis value contradicts the estimate of less than 'race_length_premise'
    label = "contradiction"
elif race_length_hypothesis < race_length_premise:
    # any race length less than 'race_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

