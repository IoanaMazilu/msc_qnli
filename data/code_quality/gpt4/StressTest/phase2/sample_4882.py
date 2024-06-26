percentage_died_premise = 1
percentage_died_hypothesis = 5
percentage_left_premise = 20
percentage_left_hypothesis = 20

# the hypothesis talks about the percentages of people who died and left the village, which are also mentioned in the premise
if percentage_died_hypothesis <= percentage_died_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentage_died_premise'
    label = "contradiction"
elif percentage_left_hypothesis != percentage_left_premise:
    # check if the percentage of people who left the village in the hypothesis contradicts the percentage of people who left the village reported in the premise
    label = "contradiction"
else:
    # any percentage of people who died greater than 'percentage_died_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
