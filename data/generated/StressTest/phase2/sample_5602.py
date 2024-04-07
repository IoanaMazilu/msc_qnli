# Premise: If Lionel's speed was less than 5 miles per hour and Walt's 6 miles per hour, how many miles had Lionel walked when he met Walt?
# Hypothesis: If Lionel's speed was 2 miles per hour and Walt's 6 miles per hour, how many miles had Lionel walked when he met Walt?
# Golden Label: neutral

lionel_speed_premise = 5
lionel_speed_hypothesis = 2
walt_speed_premise = 6
walt_speed_hypothesis = 6

# the hypothesis talks about the speed of Lionel and Walt, referenced also in the premise
if lionel_speed_hypothesis > lionel_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'lionel_speed_premise'
    label = "contradiction"
elif walt_speed_hypothesis != walt_speed_premise:
    # check if the speed of Walt in the hypothesis contradicts the speed of Walt reported in the premise
    label = "contradiction"
elif lionel_speed_hypothesis < lionel_speed_premise:
    # the premise gives an upper limit for Lionel's speed
    # any speed less than 'lionel_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

