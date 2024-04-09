race_gap_premise = 4
race_gap_hypothesis = 6
start_late_premise = 4
start_late_hypothesis = 4

# the hypothesis refers to the race gap and Karen's start delay mentioned in the premise
if race_gap_hypothesis!= race_gap_premise:
    # check if the race gap in the hypothesis contradicts the race gap reported in the premise
    label = "contradiction"
elif start_late_hypothesis!= start_late_premise:
    # check if the start delay in the hypothesis contradicts the start delay reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
