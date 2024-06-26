lilly_fish_premise = 10
rosy_fish_premise = 8
lilly_fish_hypothesis = 80

# the hypothesis refers to the number of fish Lilly has, which is mentioned in the premise
if lilly_fish_hypothesis <= lilly_fish_premise:
    # check if the estimate of 'lilly_fish_hypothesis' contradicts the number of fish in the premise
    label = "contradiction"
elif rosy_fish_hypothesis!= rosy_fish_premise:
    # check if the number of fish in the hypothesis contradicts the number of fish reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
