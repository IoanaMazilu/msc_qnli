fish_lilly_premise = 60
fish_lilly_hypothesis = 10
fish_rosy_premise = 9
fish_rosy_hypothesis = 9

# the hypothesis talks about the number of fish owned by Lilly and Rosy, referenced also in the premise
if fish_lilly_hypothesis <= fish_lilly_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fish_lilly_premise'
    label = "contradiction"
elif fish_rosy_hypothesis!= fish_rosy_premise:
    # check if the number of fish in the hypothesis contradicts the number of fish reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
