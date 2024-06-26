premise_votes_counted = 100
premise_niinisto_votes = 62.6
premise_haavisto_votes = 37.4

hypothesis_niinisto_votes = 62.6

if premise_niinisto_votes > hypothesis_niinisto_votes:
    label = "entailment"
elif premise_niinisto_votes < hypothesis_niinisto_votes:
    label = "contradiction"
else:
    label = "neutral"

print(label)
