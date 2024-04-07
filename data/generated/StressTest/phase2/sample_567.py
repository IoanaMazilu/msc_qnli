# Premise: If Lionel's speed was 3 miles per hour and Walt's 4 miles per hour, how many miles had Lionel walked when he met Walt?
# Hypothesis: If Lionel's speed was less than 4 miles per hour and Walt's 4 miles per hour, how many miles had Lionel walked when he met Walt?
# Golden Label: entailment

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

