nancy_position_premise = 6
nancy_position_hypothesis = 7

# the hypothesis talks about the position of Nancy in the row, referenced also in the premise
if nancy_position_hypothesis < nancy_position_premise:
    # check if the hypothesis value contradicts the position of Nancy in the premise
    label = "contradiction"
elif nancy_position_hypothesis > nancy_position_premise:
    # check if the hypothesis value is greater than the position of Nancy in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
