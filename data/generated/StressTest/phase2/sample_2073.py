# Premise: Zack has 3 red fish, 5 yellow fish and 7 green fish.
# Hypothesis: Zack has less than 4 red fish, 5 yellow fish and 7 green fish.
# Golden Label: entailment

red_fish_premise = 3
red_fish_hypothesis = 4
yellow_fish_premise = 5
yellow_fish_hypothesis = 5
green_fish_premise = 7
green_fish_hypothesis = 7

# the hypothesis talks about the number of each type of fish Zack has, referenced also in the premise
if red_fish_hypothesis <= red_fish_premise:
    # check if the hypothesis value contradicts the number of red fish mentioned in the premise
    label = "contradiction"
elif yellow_fish_hypothesis != yellow_fish_premise or green_fish_hypothesis != green_fish_premise:
    # check if the number of yellow or green fish in the hypothesis contradicts the number of yellow or green fish reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

