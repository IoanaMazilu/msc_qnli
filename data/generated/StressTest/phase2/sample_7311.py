# Premise: Jim runs at 6 miles per hour, and Cara runs at 5 miles per hour.
# Hypothesis: Jim runs at more than 2 miles per hour, and Cara runs at 5 miles per hour.
# Golden Label: entailment

jim_speed_premise = 6
cara_speed_premise = 5
jim_speed_hypothesis = 2
cara_speed_hypothesis = 5

# the hypothesis refers to the running speeds of Jim and Cara mentioned in the premise
if jim_speed_premise <= jim_speed_hypothesis:
    # check if the estimate of 'jim_speed_hypothesis' contradicts the speed of Jim in the premise
    label = "contradiction"
elif cara_speed_premise != cara_speed_hypothesis:
    # check if the speed of Cara in the hypothesis contradicts the speed of Cara reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

