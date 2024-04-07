# Premise: Rasik walked 20 m towards north.
# Hypothesis: Rasik walked less than 80 m towards north.
# Golden Label: entailment

distance_walked_premise = 20
distance_walked_hypothesis = 80

# the hypothesis talks about the distance walked by Rasik, referenced also in the premise
if distance_walked_premise >= distance_walked_hypothesis:
    # check if the premise value contradicts the estimate of less than 'distance_walked_hypothesis'
    label = "contradiction"
else:
    # the hypothesis suggests a maximum distance that Rasik could have walked
    # any distance less than 'distance_walked_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "entailment"

print(label)

