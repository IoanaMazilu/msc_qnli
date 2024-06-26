fish_lilly_premise = 10
fish_rosy_premise = 14
fish_lilly_hypothesis = 20
fish_rosy_hypothesis = 14

# the hypothesis refers to the number of fish Lilly and Rosy have, mentioned in the premise
if fish_lilly_premise != fish_lilly_hypothesis:
    # check if the number of fish Lilly has in the hypothesis contradicts the number of fish Lilly has in the premise
    label = "contradiction"
elif fish_rosy_premise != fish_rosy_hypothesis:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment or neutrality
    label = "entailment"

print(label)
