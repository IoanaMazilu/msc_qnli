level_premise = 3
level_hypothesis = 1
percentage_premise = 10
percentage_hypothesis = 10

# hypothesis talks about Level-1 college graduates, which is also referenced in the premise (Level-less than 3)
if level_hypothesis >= level_premise:
    # check if the level in the hypothesis contradicts the level in the premise
    label = "contradiction"
elif percentage_hypothesis != percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # The premise only gives a maximum level for the graduates, not a specific level.
    # Any level less than 'level_premise' is consistent with the premise, but cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)
