lilly_fish_premise = 10
lilly_fish_hypothesis = 30
rosy_fish_premise = 9

# the hypothesis talks about the number of fish for both Lilly and Rosy, referenced also in the premise
if lilly_fish_hypothesis <= lilly_fish_premise and rosy_fish_hypothesis <= rosy_fish_premise:
    # check if the hypothesis values for both Lilly and Rosy contradict the premise values
    label = "contradiction"
elif lilly_fish_hypothesis > lilly_fish_premise and rosy_fish_hypothesis > rosy_fish_premise:
    # check if the hypothesis values for both Lilly and Rosy are greater than the premise values
    label = "entailment"
else:
    # the premise gives only an estimate for the number of fish for both Lilly and Rosy
    # any number of fish greater than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
