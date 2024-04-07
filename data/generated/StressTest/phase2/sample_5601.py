# Premise: If Lionel's speed was 2 miles per hour and Walt's 6 miles per hour, how many miles had Lionel walked when he met Walt?
# Hypothesis: If Lionel's speed was less than 5 miles per hour and Walt's 6 miles per hour, how many miles had Lionel walked when he met Walt?
# Golden Label: entailment

lionel_speed_premise = 2
lionel_speed_hypothesis = 5
walt_speed_premise = 6
walt_speed_hypothesis = 6

# the hypothesis refers to the speed of Lionel and Walt, mentioned in the premise
if lionel_speed_hypothesis <= lionel_speed_premise:
    # check if the estimate of 'lionel_speed_hypothesis' contradicts the speed of Lionel in the premise
    label = "contradiction"
elif walt_speed_hypothesis != walt_speed_premise:
    # check if the speed of Walt in the hypothesis contradicts the speed of Walt reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

