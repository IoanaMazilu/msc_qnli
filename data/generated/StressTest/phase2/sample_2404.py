# Premise: Lilly has less than 50 fish and Rosy has 14 fish.
# Hypothesis: Lilly has 10 fish and Rosy has 14 fish.
# Golden Label: neutral

lilly_fish_premise = 50
lilly_fish_hypothesis = 10
rosy_fish_premise = 14
rosy_fish_hypothesis = 14

# the hypothesis refers to the number of fish that Lilly and Rosy have, as mentioned in the premise
if lilly_fish_hypothesis >= lilly_fish_premise:
    # check if the number of fish Lilly has in the hypothesis contradicts the estimate of less than 'lilly_fish_premise'
    label = "contradiction"
elif rosy_fish_hypothesis != rosy_fish_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fish Lilly has
    # any number of fish less than 'lilly_fish_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

