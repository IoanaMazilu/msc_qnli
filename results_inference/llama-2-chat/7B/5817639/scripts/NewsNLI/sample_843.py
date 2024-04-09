cnn_premise = "CNN"
world_title_race_premise = 14

# the premise mentions the news source and the lead in the world title race, which are also referenced in the hypothesis
if cnn_hypothesis == cnn_premise:
    # check if the hypothesis and premise mention the same news source
    label = "entailment"
elif world_title_race_hypothesis > world_title_race_premise:
    # check if the lead in the hypothesis contradicts the lead in the premise
    label = "contradiction"
else:
    # if the hypothesis and premise do not mention the same news source or lead, we can infer neutrality
    label = "neutral"

print(label)
