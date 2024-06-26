lilly_fish_premise = 80
rosy_fish_premise = 8
lilly_fish_hypothesis = 10
rosy_fish_hypothesis = 8

# the hypothesis refers to the number of fish Lilly and Rosy have, which are also mentioned in the premise
if lilly_fish_hypothesis <= lilly_fish_premise and rosy_fish_hypothesis <= rosy_fish_premise:
    # check if the number of fish in the hypothesis contradicts the number of fish in the premise
    label = "contradiction"
elif lilly_fish_hypothesis > lilly_fish_premise or rosy_fish_hypothesis > rosy_fish_premise:
    # if the number of fish in the hypothesis is greater than the number of fish in the premise, it is a contradiction
    label = "contradiction"
else:
    # if the number of fish in the hypothesis is less than or equal to the number of fish in the premise, it is a neutral case
    label = "neutral"

print(label)
