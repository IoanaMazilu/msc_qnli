# Premise: Suraj has a certain average of runs for 12 innings.
# Hypothesis: Suraj has a certain average of runs for 42 innings.
# Golden Label: contradiction

innings_premise = 12
innings_hypothesis = 42

# the hypothesis talks about the number of innings, referenced also in the premise
if innings_hypothesis != innings_premise:
    # check if the number of innings in the hypothesis contradicts the number of innings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

