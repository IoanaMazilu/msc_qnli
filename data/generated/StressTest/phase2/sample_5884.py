# Premise: Anusha, Banu and Esha run a running race of less than 800 meters.
# Hypothesis: Anusha, Banu and Esha run a running race of 100 meters.
# Golden Label: neutral

race_distance_premise = 800
race_distance_hypothesis = 100

# The hypothesis talks about the exact distance of the race run by Anusha, Banu and Esha, which is also referenced in the premise
if race_distance_hypothesis >= race_distance_premise:
    # Check if the hypothesis value contradicts the premise's estimate of less than 'race_distance_premise' meters
    label = "contradiction"
else:
    # The premise gives only an estimate for the distance of the race
    # Any distance less than 'race_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

