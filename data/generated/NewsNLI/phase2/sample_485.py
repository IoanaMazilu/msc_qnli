# Premise: The attack took place at a Suncor Energy base plant, 200 miles north of Edmonton.
# Hypothesis: The latest attack took place 200 miles north of Edmonton.
# Golden Label: neutral

distance_premise = 200
distance_hypothesis = 200

# the hypothesis mentions the distance of the attack from Edmonton, which is also referenced in the premise
# however, the hypothesis does not specify the place of the attack, which is specified in the premise
label = "neutral"

print(label)
