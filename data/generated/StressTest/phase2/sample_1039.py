# Premise: If Lionel's speed was less than 4 miles per hour and Walt's 3 miles per hour, how many miles had Lionel walked when he met Walt?
# Hypothesis: If Lionel's speed was 3 miles per hour and Walt's 3 miles per hour, how many miles had Lionel walked when he met Walt?
# Golden Label: neutral

lionel_speed_premise = 4
lionel_speed_hypothesis = 3
walt_speed_premise = 3
walt_speed_hypothesis = 3

# the hypothesis talks about the speed of Lionel and Walt, which is also referenced in the premise
if lionel_speed_hypothesis >= lionel_speed_premise:
    # check if Lionel's speed in the hypothesis contradicts the estimate of less than 'lionel_speed_premise'
    label = "contradiction"
elif walt_speed_hypothesis != walt_speed_premise:
    # check if Walt's speed in the hypothesis contradicts Walt's speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

