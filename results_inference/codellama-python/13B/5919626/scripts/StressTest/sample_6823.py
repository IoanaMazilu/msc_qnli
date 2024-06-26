lilly_fish_premise = 80
lilly_fish_hypothesis = 10
rosy_fish_premise = 8
rosy_fish_hypothesis = 8

# the hypothesis talks about the number of fish in a vase, referenced also in the premise
if lilly_fish_hypothesis >= lilly_fish_premise:
    # check if the hypothesis value contradicts the estimate of less than 'lilly_fish_premise'
    label = "contradiction"
elif rosy_fish_hypothesis!= rosy_fish_premise:
    # check if the number of fish in the hypothesis contradicts the number of fish in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fish
    # any number of fish greater than 'rosy_fish_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
