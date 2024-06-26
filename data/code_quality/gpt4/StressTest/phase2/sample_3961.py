lionel_speed_premise = 7
lionel_speed_hypothesis = 3
walt_speed_premise = 6
walt_speed_hypothesis = 6

# the hypothesis talks about the speed of Lionel and Walt, referenced also in the premise
if lionel_speed_hypothesis >= lionel_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'lionel_speed_premise'
    label = "contradiction"
elif walt_speed_hypothesis != walt_speed_premise:
    # check if the speed of Walt in the hypothesis contradicts the speed of Walt reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Lionel
    # any speed of Lionel less than 'lionel_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
