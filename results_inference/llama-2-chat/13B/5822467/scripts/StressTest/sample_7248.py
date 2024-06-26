lilly_fish_premise = 10
lilly_fish_hypothesis = 9
rosy_fish_premise = 9

# the hypothesis refers to the number of fish owned by Lilly and Rosy
if lilly_fish_hypothesis <= lilly_fish_premise and rosy_fish_hypothesis == rosy_fish_premise:
    # check if the hypothesis values for Lilly and Rosy do not contradict the premise values
    label = "entailment"
elif lilly_fish_hypothesis > lilly_fish_premise:
    # check if the estimate of 'lilly_fish_hypothesis' contradicts the number of fish owned by Lilly in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fish owned by Lilly and Rosy
    # any number of fish less than or equal to 60 for Lilly and 9 for Rosy is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
