lionel_speed_premise = 2
lionel_speed_hypothesis = 3
walt_speed_premise = 6
walt_speed_hypothesis = 6

# The hypothesis discusses about Lionel's and Walt's speed, referenced also in the premise
if lionel_speed_hypothesis < lionel_speed_premise:
    # check if the hypothesis value contradicts Lionel's speed in the premise
    label = "contradiction"
elif walt_speed_hypothesis != walt_speed_premise:
    # check if Walt's speed in the hypothesis contradicts Walt's speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
