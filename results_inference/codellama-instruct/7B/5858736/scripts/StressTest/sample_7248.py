lilly_fish_premise = 10
rosy_fish_premise = 9
lilly_fish_hypothesis = 60
rosy_fish_hypothesis = 9

# the hypothesis talks about the number of fish in Lilly and Rosy, referenced also in the premise
if lilly_fish_hypothesis >= lilly_fish_premise:
    # check if the hypothesis value contradicts the estimate of less than 'lilly_fish_premise'
    label = "contradiction"
elif rosy_fish_hypothesis!= rosy_fish_premise:
    # check if the number of fish in Rosy in the hypothesis contradicts the number of fish reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)