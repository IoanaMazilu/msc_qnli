# Premise: Lilly has less than 60 fish and Rosy has 9 fish.
# Hypothesis: Lilly has 10 fish and Rosy has 9 fish.
# Golden Label: neutral

fish_lilly_premise = 60
fish_lilly_hypothesis = 10
fish_rosy_premise = 9
fish_rosy_hypothesis = 9

# the hypothesis refers to the number of fish Lilly and Rosy have, as mentioned in the premise
if fish_lilly_hypothesis >= fish_lilly_premise:
    # check if the number of fish Lilly has in the hypothesis contradicts the premise's statement of Lilly having less than 'fish_lilly_premise' fish
    label = "contradiction"
elif fish_rosy_hypothesis != fish_rosy_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of fish Lilly has, but the exact number of fish Rosy has
    # any number of fish less than 'fish_lilly_premise' for Lilly and exactly 'fish_rosy_premise' fish for Rosy is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

