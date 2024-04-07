# Premise: Karen places a bet with Tom that she will beat Tom in a car race by 4 miles even if Karen starts 4 minutes late.
# Hypothesis: Karen places a bet with Tom that she will beat Tom in a car race by more than 4 miles even if Karen starts 4 minutes late.
# Golden Label: contradiction

miles_premise = 4
miles_hypothesis = 4
minutes_late_premise = 4
minutes_late_hypothesis = 4

# the hypothesis refers to the miles and minutes late mentioned in the premise
if miles_hypothesis > miles_premise:
    # check if the estimate of 'miles_hypothesis' contradicts the number of miles in the premise
    label = "contradiction"
elif minutes_late_hypothesis != minutes_late_premise:
    # check if the number of minutes late in the hypothesis contradicts the number of minutes late reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

