# Premise: If Shreehari walks in the speed of 4.5 km/hr from his house, in what time will he reach his school which is 750 m long from his house?
# Hypothesis: If Shreehari walks in the speed of 4.5 km/hr from his house, in what time will he reach his school which is 550 m long from his house?
# Golden Label: contradiction

distance_to_school_premise = 750
distance_to_school_hypothesis = 550

# the hypothesis talks about the distance of the school from Shreehari's house, which is also mentioned in the premise
if distance_to_school_hypothesis != distance_to_school_premise:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

