# Premise: Zack has less than 4 red fish, 5 yellow fish and 7 green fish.
# Hypothesis: Zack has 3 red fish, 5 yellow fish and 7 green fish.
# Golden Label: neutral

red_fish_premise = 4
red_fish_hypothesis = 3
yellow_fish_premise = 5
yellow_fish_hypothesis = 5
green_fish_premise = 7
green_fish_hypothesis = 7

# the hypothesis refers to the number of red, yellow and green fish Zack has, mentioned also in the premise
if red_fish_hypothesis >= red_fish_premise:
    # check if the number of red fish in the hypothesis contradicts the premise (less than 'red_fish_premise')
    label = "contradiction"
elif yellow_fish_hypothesis != yellow_fish_premise or green_fish_hypothesis != green_fish_premise:
    # check if the number of yellow or green fish in the hypothesis contradicts the number of yellow or green fish reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

