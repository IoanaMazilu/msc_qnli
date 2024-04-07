# Premise: less than 70% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Hypothesis: 10% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Golden Label: neutral

death_rate_premise = 70
death_rate_hypothesis = 10
flee_rate = 20

# the hypothesis talks about the death and flee rates in a village, referenced also in the premise
if death_rate_hypothesis >= death_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'death_rate_premise'
    label = "contradiction"
elif flee_rate != flee_rate:
    # check if the flee rate in the hypothesis contradicts the flee rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the death rate
    # any death rate less than 'death_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

