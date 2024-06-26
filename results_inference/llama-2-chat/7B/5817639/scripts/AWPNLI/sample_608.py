geese_premise = 58.0
ducks_premise = 37.0
additional_geese_hypothesis = 21.0

# compare the number of geese in the hypothesis to the number of geese in the premise
if additional_geese_hypothesis > geese_premise:
    label = "entailment"
elif additional_geese_hypothesis < geese_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
