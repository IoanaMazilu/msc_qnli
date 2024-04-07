# Premise: Raj and Roshan has some money with them in the ratio less than 8:4 respectively.
# Hypothesis: Raj and Roshan has some money with them in the ratio 5:4 respectively.
# Golden Label: neutral

raj_roshan_ratio_premise = 8 / 4
raj_roshan_ratio_hypothesis = 5 / 4

# the hypothesis talks about the money ratio of Raj and Roshan, referenced also in the premise
if raj_roshan_ratio_hypothesis >= raj_roshan_ratio_premise:
    # check if the hypothesis ratio contradicts the estimate of less than 'raj_roshan_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'raj_roshan_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

