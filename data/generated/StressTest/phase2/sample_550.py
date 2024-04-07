# Premise: Aamir saves less than 42% of his monthly salary.
# Hypothesis: Aamir saves 32% of his monthly salary.
# Golden Label: neutral

savings_premise = 42
savings_hypothesis = 32

# the hypothesis talks about the percentage of salary that Aamir saves, referenced also in the premise
if savings_hypothesis >= savings_premise:
    # check if the hypothesis value contradicts the estimate of less than 'savings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of salary Aamir saves
    # any percentage less than 'savings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

