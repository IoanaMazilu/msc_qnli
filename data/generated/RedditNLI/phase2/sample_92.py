# Premise: Deutsche Bank Slapped With $14 Billion Fine By DOJ Over Mortgage Probe.
# Hypothesis: Deutsche Bank Rebuffs U.S. Over $14 Billion Mortgage Settlement.
# Golden Label: neutral

fine_premise = 14e9
fine_hypothesis = 14e9

# the hypothesis and premise both mention the amount of a fine
if fine_hypothesis != fine_premise:
    # check if the fine amount in the hypothesis contradicts the fine amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

