# Premise: Chile moved onto nine points from five matches with a 2-0 win over bottom team Bolivia, who had Luis Gutierrez sent off in the second half.
# Hypothesis: Chile in second place after 2-0 win against bottom nation Bolivia.
# Golden Label: neutral

chile_points_premise = 9
chile_matches_premise = 5
chile_score_premise = 2
bolivia_score_premise = 0

# The hypothesis mentions Chile's score and the opposing team, which are also mentioned in the premise
# However, the hypothesis states Chile's place in the ranking, which cannot be entailed from the premise
label = "neutral"

print(label)

