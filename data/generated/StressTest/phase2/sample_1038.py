# Premise: If Lionel's speed was 3 miles per hour and Walt's 3 miles per hour, how many miles had Lionel walked when he met Walt?
# Hypothesis: If Lionel's speed was less than 4 miles per hour and Walt's 3 miles per hour, how many miles had Lionel walked when he met Walt?
# Golden Label: entailment

lionel_speed_premise = 3
walt_speed_premise = 3
lionel_speed_hypothesis = 4
walt_speed_hypothesis = 3

# the hypothesis refers to Lionel's and Walt's speed mentioned in the premise
if lionel_speed_premise >= lionel_speed_hypothesis:
    # check if the estimate of 'lionel_speed_hypothesis' contradicts the Lionel's speed in the premise
    label = "contradiction"
elif walt_speed_hypothesis != walt_speed_premise:
    # check if the Walt's speed in the hypothesis contradicts the Walt's speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

