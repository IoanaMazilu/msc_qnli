lilly_fish_premise = 10
lilly_fish_hypothesis = 60
rosy_fish_premise = 9
rosy_fish_hypothesis = 9

# the hypothesis talks about the number of fish owned by Lilly and Rosy
if lilly_fish_hypothesis <= lilly_fish_premise:
    # check if the hypothesis value contradicts the estimate of 'lilly_fish_premise'
    label = "contradiction"
elif rosy_fish_hypothesis!= rosy_fish_premise:
    # check if the number of fish owned by Rosy in the hypothesis contradicts the number of fish owned by Rosy in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
