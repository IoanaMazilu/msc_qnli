lilly_fish_premise = 10
rosy_fish_premise = 8
lilly_fish_hypothesis = 79
rosy_fish_hypothesis = 8

# the hypothesis talks about the number of fish for both Lilly and Rosy
if lilly_fish_hypothesis <= lilly_fish_premise and rosy_fish_hypothesis == rosy_fish_premise:
    # check if the hypothesis values for both Lilly and Rosy do not contradict the premise values
    label = "entailment"
elif lilly_fish_hypothesis > lilly_fish_premise:
    # check if the estimate of 'lilly_fish_hypothesis' contradicts the number of fish reported in the premise for Lilly
    label = "contradiction"
elif rosy_fish_hypothesis!= rosy_fish_premise:
    # check if the number of fish reported in the hypothesis for Rosy contradicts the number of fish reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
