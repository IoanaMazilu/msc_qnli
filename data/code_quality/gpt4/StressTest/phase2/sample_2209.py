fish_lilly_premise = 20
fish_lilly_hypothesis = 10
fish_rosy_premise = 12
fish_rosy_hypothesis = 12

# the hypothesis refers to the number of fish Lilly and Rosy have, mentioned in the premise
if fish_lilly_hypothesis >= fish_lilly_premise:
    # check if the number of fish Lilly has in the hypothesis contradicts the premise of Lilly having less than 'fish_lilly_premise' fish
    label = "contradiction"
elif fish_rosy_hypothesis != fish_rosy_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    label = "contradiction"
elif fish_lilly_hypothesis > fish_lilly_premise:
    # check if the number of fish Lilly has in the hypothesis is more than the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
