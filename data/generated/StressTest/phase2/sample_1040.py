# Premise: If Lionel's speed was 3 miles per hour and Walt's 3 miles per hour, how many miles had Lionel walked when he met Walt?
# Hypothesis: If Lionel's speed was more than 3 miles per hour and Walt's 3 miles per hour, how many miles had Lionel walked when he met Walt?
# Golden Label: contradiction

lionel_speed_premise = 3
walt_speed_premise = 3
lionel_speed_hypothesis = 3
walt_speed_hypothesis = 3

# the hypothesis refers to the speed of Lionel and Walt mentioned in the premise
if lionel_speed_premise >= lionel_speed_hypothesis:
    # check if the statement 'lionel_speed_hypothesis' contradicts the speed of Lionel in the premise
    label = "contradiction"
elif walt_speed_hypothesis != walt_speed_premise:
    # check if the speed of Walt in the hypothesis contradicts the speed of Walt reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

