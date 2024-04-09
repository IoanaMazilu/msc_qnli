lilly_fish_premise = 10
lilly_fish_hypothesis = 40
rosy_fish_premise = 8

# the hypothesis refers to the number of fish owned by Lilly and Rosy
if lilly_fish_premise <= lilly_fish_hypothesis and rosy_fish_premise == rosy_fish_hypothesis:
    # check if the estimate of 'lilly_fish_hypothesis' and 'rosy_fish_hypothesis' do not contradict the premise
    label = "entailment"
elif lilly_fish_hypothesis!= lilly_fish_premise or rosy_fish_hypothesis!= rosy_fish_premise:
    # check if the number of fish in the hypothesis contradicts the number of fish reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
