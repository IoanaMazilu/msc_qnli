# Premise
sister_castle_height_premise = 0.5
miki_castle_height_premise = 0.8333333333333334
total_castle_height_premise = sister_castle_height_premise + miki_castle_height_premise

# Hypothesis
total_castle_height_hypothesis = 1.33333333333

# Variables
sister_castle_height = 0.5
miki_castle_height = 0.8333333333333334

# Comparison
if total_castle_height_hypothesis!= total_castle_height_premise:
    label = "contradiction"
elif sister_castle_height!= sister_castle_height_premise or miki_castle_height!= miki_castle_height_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
