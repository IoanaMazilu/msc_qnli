# Premise: Suraj has a certain average of runs for 9 innings.
# Hypothesis: Suraj has a certain average of runs for 1 innings.
# Golden Label: contradiction

innings_played_premise = 9
innings_played_hypothesis = 1

# the hypothesis refers to the number of innings played by Suraj, mentioned also in the premise
if innings_played_premise != innings_played_hypothesis:
    # check if the number of innings in the hypothesis contradicts the number of innings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

