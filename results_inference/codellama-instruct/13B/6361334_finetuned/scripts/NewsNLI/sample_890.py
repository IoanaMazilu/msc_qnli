wins_premise = 0
losses_premise = 11
wins_hypothesis = 1
losses_hypothesis = 0

# the hypothesis mentions a win for Celtic in Moscow, which is not mentioned in the premise
# the premise mentions Celtic's record of 11 straight losses on the road in the Champions League and 21 games without a win away from home
# the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from it
label = "neutral"

print(label)
