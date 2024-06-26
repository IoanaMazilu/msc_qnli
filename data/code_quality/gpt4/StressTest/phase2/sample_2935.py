lionel_speed_premise = 3
lionel_speed_hypothesis = 2
walt_speed_premise = 6
walt_speed_hypothesis = 6

# the hypothesis talks about the speeds of Lionel and Walt, which is also referenced in the premise
if lionel_speed_hypothesis > lionel_speed_premise:
    # check if the speed of Lionel in the hypothesis contradicts the estimate of less than 'lionel_speed_premise'
    label = "contradiction"
elif walt_speed_hypothesis != walt_speed_premise:
    # check if the speed of Walt in the hypothesis contradicts the speed of Walt mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
