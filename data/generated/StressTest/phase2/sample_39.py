# Premise: A runner runs the 40 miles from Marathon to Athens at a constant speed.
# Hypothesis: A runner runs the more than 20 miles from Marathon to Athens at a constant speed.
# Golden Label: entailment

distance_premise = 40
distance_hypothesis = 20

# the hypothesis talks about the distance from Marathon to Athens, referenced also in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the exact distance 'distance_premise' 
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # any distance smaller than 'distance_premise' is consistent with the premise, and can be explicitly entailed from the premise because the premise gives the exact distance
    label = "entailment"

print(label)

