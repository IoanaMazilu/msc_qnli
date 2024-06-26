lilly_fish_premise = 10
lilly_fish_hypothesis = 30
rosy_fish_premise = 9
rosy_fish_hypothesis = 9

# the hypothesis talks about the number of fish in both Lilly and Rosy
if lilly_fish_hypothesis <= lilly_fish_premise and rosy_fish_hypothesis <= rosy_fish_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fish in both Lilly and Rosy
    # any number of fish greater than the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
