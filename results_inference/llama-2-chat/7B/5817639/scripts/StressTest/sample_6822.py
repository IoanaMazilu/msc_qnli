lilly_fish_premise = 10
lilly_fish_hypothesis = 80
rosy_fish_premise = 8
rosy_fish_hypothesis = 8

# the hypothesis talks about the number of fish owned by Lilly and Rosy
if lilly_fish_hypothesis <= rosy_fish_premise:
    # check if the hypothesis value contradicts the estimate of 'rosy_fish_premise'
    label = "contradiction"
elif lilly_fish_hypothesis > rosy_fish_premise:
    # check if the hypothesis value entails the estimate of 'rosy_fish_premise'
    label = "entailment"
else:
    # neither the hypothesis nor the premise provides enough information to determine entailment or contradiction
    label = "neutral"

print(label)
