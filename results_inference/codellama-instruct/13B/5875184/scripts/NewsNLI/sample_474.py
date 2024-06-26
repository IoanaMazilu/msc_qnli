matches_premise = 23
impressions_premise = 1
relegation_premise = 1

matches_hypothesis = 23
impressions_hypothesis = 1
relegation_hypothesis = 1

if impressions_hypothesis!= impressions_premise:
    label = "contradiction"
elif relegation_hypothesis!= relegation_premise:
    label = "neutral"
else:
    label = "entailment"

print(label)
