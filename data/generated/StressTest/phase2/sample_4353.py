# Premise: Karen places a bet with Tom that she will beat Tom in a car race by 4 miles even if Karen starts 4 minutes late.
# Hypothesis: Karen places a bet with Tom that she will beat Tom in a car race by less than 6 miles even if Karen starts 4 minutes late.
# Golden Label: entailment

race_gap_premise = 4
race_gap_hypothesis = 6
start_late_premise = 4
start_late_hypothesis = 4

# the hypothesis refers to the gap by which Karen will beat Tom and the delay of Karen's start, both mentioned in the premise
if race_gap_hypothesis < race_gap_premise:
    # check if the hypothesis value contradicts the value of 'race_gap_premise'
    label = "contradiction"
elif start_late_hypothesis != start_late_premise:
    # check if the delay of Karen's start in the hypothesis contradicts the delay reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, but the gap in the race is estimated to be less in the hypothesis
    # it can be inferred as entailment
    label = "entailment"

print(label)

