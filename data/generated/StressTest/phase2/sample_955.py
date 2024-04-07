# Premise: less than 85% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Hypothesis: 15% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Golden Label: neutral

died_premise = 85
died_hypothesis = 15

# the hypothesis talks about the percentage of people died and left, referenced also in the premise
if died_hypothesis >= died_premise:
    # check if the hypothesis value contradicts the estimate of less than 'died_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of people died
    # any percentage of people died less than 'died_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

