# Premise: Jack and Christina are standing 240 feet apart on a level surface.
# Hypothesis: Jack and Christina are standing less than 440 feet apart on a level surface.
# Golden Label: entailment

distance_apart_premise = 240
distance_apart_hypothesis = 440

# the hypothesis refers to the distance between Jack and Christina mentioned in the premise
if distance_apart_hypothesis < distance_apart_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif distance_apart_hypothesis == distance_apart_premise:
    # if the distances in the premise and hypothesis are equal, we can infer entailment
    label = "entailment"
else:
    # if the distance in the hypothesis is greater than the distance in the premise, we can infer neutrality
    # since the premise does not provide information about a distance larger than 'distance_apart_premise'
    label = "neutral"

print(label)

