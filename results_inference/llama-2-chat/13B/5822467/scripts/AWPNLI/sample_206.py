fishbowls_premise = 261.0
fish_per_bowl_premise = 23.0
total_fish_hypothesis = 6003.0

# compute the total number of fish in the premise
total_fish_premise = fishbowls_premise * fish_per_bowl_premise

if total_fish_hypothesis > total_fish_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif total_fish_hypothesis < total_fish_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise are neutral
    label = "neutral"

print(label)
