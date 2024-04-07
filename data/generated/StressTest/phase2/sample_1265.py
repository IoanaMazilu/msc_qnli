# Premise: If they work in stretches of one hour alternately, Vikas beginning at 8 a.
# Hypothesis: If they work in stretches of one hour alternately, Vikas beginning at more than 8 a.
# Golden Label: contradiction

start_time_vikas_premise = 8
start_time_vikas_hypothesis = 8

# the hypothesis refers to the start time of Vikas's work, mentioned in the premise
if start_time_vikas_hypothesis > start_time_vikas_premise:
    # check if the start time in the hypothesis contradicts the start time reported in the premise
    label = "contradiction"
elif start_time_vikas_hypothesis < start_time_vikas_premise:
    # check if the start time in the hypothesis is less than the start time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

