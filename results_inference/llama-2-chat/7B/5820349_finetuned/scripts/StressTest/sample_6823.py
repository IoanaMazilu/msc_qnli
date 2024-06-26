fish_lilly_premise = 80
fish_lilly_hypothesis = 10
fish_rosy_premise = 8
fish_rosy_hypothesis = 8

# the hypothesis refers to the number of fish Lilly and Rosy have, mentioned in the premise
if fish_lilly_hypothesis >= fish_lilly_premise:
    # check if the number of fish Lilly has in the hypothesis contradicts the estimate of less than 'fish_lilly_premise'
    label = "contradiction"
elif fish_rosy_hypothesis!= fish_rosy_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fish Lilly has
    # any number of fish less than 'fish_lilly_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
