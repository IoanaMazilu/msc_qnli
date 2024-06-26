fish_lilly_premise = 10
fish_rosy_premise = 12
fish_lilly_hypothesis = 10
fish_rosy_hypothesis = 12

# the hypothesis specifies the number of fish both Lilly and Rosy have, referenced also in the premise
if fish_lilly_hypothesis >= fish_lilly_premise:
    # check if the hypothesis value contradicts the exact number of fish Lilly has in the premise
    label = "contradiction"
elif fish_rosy_hypothesis != fish_rosy_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
