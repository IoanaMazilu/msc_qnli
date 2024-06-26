lionel_speed_premise = 3
lionel_speed_hypothesis = 4
walt_speed_premise = 4
walt_speed_hypothesis = 4

# the hypothesis refers to the speed of Lionel and Walt, also mentioned in the premise
if lionel_speed_premise >= lionel_speed_hypothesis or walt_speed_premise != walt_speed_hypothesis:
    # check if the speed of Lionel or Walt in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
