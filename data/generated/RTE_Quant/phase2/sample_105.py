# Premise: Scientists on Monday announced the discovery of a frozen, shiny red world some 8 billion miles from Earth that is the most distant known object in the solar system.
# Hypothesis: A frozen world 8 billion miles from Earth is believed to be the farthest known object within our solar system.
# Golden Label: entailment

distance_premise = 8e9 # miles
distance_hypothesis = 8e9 # miles

# the hypothesis talks about the distance of the most distant known object in the solar system which is also mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance value in the hypothesis does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

