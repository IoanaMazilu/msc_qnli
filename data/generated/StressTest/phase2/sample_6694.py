# Premise: less than 44000 after 8 months, John withdraws Rs.
# Hypothesis: 14000 after 8 months, John withdraws Rs.
# Golden Label: neutral

withdraw_premise = 44000
withdraw_hypothesis = 14000

# the hypothesis speaks about the amount John withdraws after 8 months which is also mentioned in the premise
if withdraw_hypothesis >= withdraw_premise:
    # check if the 'withdraw_hypothesis' value contradicts the estimation of less than 'withdraw_premise'
    label = "contradiction"
else:
    # the premise gives only an estimation for the withdrawal
    # any withdrawal less than 'withdraw_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

