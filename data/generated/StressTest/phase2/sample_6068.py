# Premise: There was 4 to 5 shops in the town which was build by a builder from Mumbai.
# Hypothesis: There was less than 4 to 5 shops in the town which was build by a builder from Mumbai.
# Golden Label: contradiction

shops_town_premise = 4
shops_town_hypothesis = 4

# The hypothesis discusses the number of shops in the town, which is also mentioned in the premise
if shops_town_hypothesis >= shops_town_premise:
    # Check if the hypothesis value contradicts the premise of having 'shops_town_premise' to 'shops_town_premise + 1' shops
    label = "contradiction"
else:
    # If the number of shops in the hypothesis is less than 'shops_town_premise', it contradicts the premise
    label = "entailment"

print(label)

