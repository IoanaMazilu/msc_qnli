# Premise: Zvonareva will face another Czech in the next round after Petra Kvitova edged out Italy's Flavia Pennetta 3-6 6-3 6-3.
# Hypothesis: Petra Kvitova edges out Flavia Penetta 3-6 6-3 6-3 to advance to the next round.
# Golden Label: entailment

# score variables for Petra Kvitova and Flavia Pennetta
kvitova_score_premise = [3, 6, 6]
pennetta_score_premise = [6, 3, 3]

kvitova_score_hypothesis = [3, 6, 6]
pennetta_score_hypothesis = [6, 3, 3]

# Check if the scores in the hypothesis contradict or entail the scores in the premise
if kvitova_score_hypothesis != kvitova_score_premise or pennetta_score_hypothesis != pennetta_score_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)

