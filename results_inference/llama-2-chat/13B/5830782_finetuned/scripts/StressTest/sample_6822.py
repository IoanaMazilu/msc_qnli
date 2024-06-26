fish_lilly_premise = 10
fish_rosy_premise = 8
fish_lilly_hypothesis = 80
fish_rosy_hypothesis = 8

# the hypothesis refers to the number of fish Lilly and Rosy have, as mentioned in the premise
if fish_lilly_premise >= fish_lilly_hypothesis:
    # check if the estimate of 'fish_lilly_hypothesis' contradicts the number of fish Lilly has in the premise
    label = "contradiction"
elif fish_rosy_hypothesis!= fish_rosy_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
