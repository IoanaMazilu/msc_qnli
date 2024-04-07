# Premise: There are 28 stations between Kolkatta and Chennai.
# Hypothesis: There are less than 28 stations between Kolkatta and Chennai.
# Golden Label: contradiction

stations_premise = 28
stations_hypothesis = 28

# the hypothesis references the number of stations between two cities mentioned in the premise
if stations_hypothesis < stations_premise:
    # check if the hypothesis value contradicts the exact number of 'stations_premise'
    label = "contradiction"
elif stations_hypothesis == stations_premise:
    # if the hypothesis value equals the premise one, we can infer entailment
    label = "entailment"
else:
    # any number of stations greater than 'stations_premise' cannot be inferred from the premise
    label = "neutral"

print(label)

