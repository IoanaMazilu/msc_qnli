lionel_speed_premise = 2
lionel_speed_hypothesis = 2
walt_speed_premise = 6
walt_speed_hypothesis = 6

# the hypothesis talks about Lionel's and Walt's speed, referenced also in the premise
if lionel_speed_hypothesis >= lionel_speed_premise:
    # check if the hypothesis value contradicts the premise of Lionel's speed being less than 'lionel_speed_premise'
    label = "contradiction"
elif walt_speed_hypothesis != walt_speed_premise:
    # check if the speed of Walt in the hypothesis contradicts the speed of Walt reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
