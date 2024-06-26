lilly_fish_premise = 10
rosy_fish_premise = 9
lilly_fish_hypothesis = 60
rosy_fish_hypothesis = 9

# the hypothesis refers to the number of fish Lilly and Rosy have, mentioned in the premise
if lilly_fish_premise >= lilly_fish_hypothesis:
    # check if the estimate of 'lilly_fish_hypothesis' contradicts the number of fish Lilly has in the premise
    label = "contradiction"
elif rosy_fish_hypothesis!= rosy_fish_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
