lilly_fish_premise = 80
lilly_fish_hypothesis = 10
rosy_fish_premise = 8
rosy_fish_hypothesis = 8

# the hypothesis talks about the number of fish Lilly and Rosy have, referenced also in the premise
if lilly_fish_hypothesis >= lilly_fish_premise:
    # check if the number of fish Lilly has in the hypothesis contradicts the estimate of less than 'lilly_fish_premise'
    label = "contradiction"
elif rosy_fish_hypothesis!= rosy_fish_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
