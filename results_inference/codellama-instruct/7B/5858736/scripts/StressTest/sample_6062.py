Anita_goes_away_premise = True
Indu_leaves_premise = 7
Anita_goes_away_hypothesis = True
Indu_leaves_hypothesis = 10

if Anita_goes_away_premise == Anita_goes_away_hypothesis and Indu_leaves_premise <= Indu_leaves_hypothesis:
    label = "entailment"
else:
    label = "contradiction"

print(label)
