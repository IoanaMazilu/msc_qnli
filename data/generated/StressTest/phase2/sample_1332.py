# Premise: In covering a distance of 30 km, Arun takes 2 hours more than Anil.
# Hypothesis: In covering a distance of less than 50 km, Arun takes 2 hours more than Anil.
# Golden Label: entailment

distance_premise = 30
distance_hypothesis = 50
extra_time = 2

# the hypothesis talks about the same situation mentioned in the premise, but with a different distance
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the distance value in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # the premise gives a specific distance, while the hypothesis gives a higher estimate
    # the extra time Arun takes is the same in both sentences
    # hence, the premise cannot explicitly entail the hypothesis
    label = "neutral"

print(label)

