# Premise: Survey Finds that Black Business Ownership in the US Jumped 400% in One Year.
# Hypothesis: Black Business Ownership Under Trump Jumps 400% in one year.
# Golden Label: neutral

percentage_increase_premise = 400
percentage_increase_hypothesis = 400

# the hypothesis and premise mention the percentage increase in black business ownership in one year
if percentage_increase_hypothesis != percentage_increase_premise:
    # check if the percentage increase in the hypothesis contradicts the percentage increase in the premise
    label = "contradiction"
else:
    # the premise does not specify under which administration the increase happened
    # the hypothesis' mention of the Trump administration is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

