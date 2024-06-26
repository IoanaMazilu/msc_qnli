withdrawal_premise = 14000
withdrawal_hypothesis = 44000

# the hypothesis refers to the amount John withdraws after 8 months, mentioned in the premise
if withdrawal_hypothesis >= withdrawal_premise:
    # check if the hypothesis value contradicts the amount withdrawn in the premise
    label = "contradiction"
elif withdrawal_hypothesis < withdrawal_premise:
    # check if the hypothesis value is less than the amount withdrawn in the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the amount withdrawn in the premise, it cannot be explicitly entailed
    label = "neutral"

print(label)
