fish_lilly_premise = 80
fish_rosy_premise = 8
fish_lilly_hypothesis = 10
fish_rosy_hypothesis = 8

# the hypothesis talks about the number of fishes Lilly and Rosy have, referenced also in the premise
if fish_lilly_hypothesis >= fish_lilly_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fish_lilly_premise'
    label = "contradiction"
elif fish_rosy_hypothesis!= fish_rosy_premise:
    # check if the number of fishes Rosy has in the hypothesis contradicts the number of fishes Rosy has reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fishes Lilly has
    # any number of fishes less than 'fish_lilly_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
