fish_lilly_premise = 10
fish_rosy_premise = 8
fish_lilly_hypothesis = 40
fish_rosy_hypothesis = 8

# the hypothesis refers to the number of fishes Lilly and Rosy have, which is also mentioned in the premise
if fish_lilly_hypothesis!= fish_lilly_premise:
    # check if the number of fishes Lilly has in the hypothesis contradicts the number of fishes Lilly has in the premise
    label = "contradiction"
elif fish_rosy_hypothesis!= fish_rosy_premise:
    # check if the number of fishes Rosy has in the hypothesis contradicts the number of fishes Rosy has in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)