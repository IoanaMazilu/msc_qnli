# Premise: If Anne’s speed were doubled, they could clean their house in 3 hours working at their respective rates.
# Hypothesis: If Anne’s speed were doubled, they could clean their house in 8 hours working at their respective rates.
# Golden Label: contradiction

cleaning_time_doubled_speed_premise = 3
cleaning_time_doubled_speed_hypothesis = 8

# the hypothesis refers to the cleaning time if Anne's speed were doubled, also mentioned in the premise
if cleaning_time_doubled_speed_hypothesis != cleaning_time_doubled_speed_premise:
    # check if the cleaning time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

