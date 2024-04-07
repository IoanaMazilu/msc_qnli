# Premise: Suraj has a certain average of runs for 16 innings.
# Hypothesis: Suraj has a certain average of runs for 66 innings.
# Golden Label: contradiction

innings_premise = 16
innings_hypothesis = 66

# the hypothesis talks about the average runs for a different number of innings than the premise
if innings_hypothesis != innings_premise:
    # check if the number of innings in the hypothesis contradicts the number of innings reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same number of innings, so we can infer entailment
    label = "entailment"

print(label)

