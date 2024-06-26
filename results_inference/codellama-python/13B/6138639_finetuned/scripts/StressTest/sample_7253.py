innings_premise = 8
innings_hypothesis = 4

# the hypothesis talks about the number of innings for which Suraj has a certain average of runs, referenced also in the premise
if innings_hypothesis!= innings_premise:
    # check if the number of innings in the hypothesis contradicts the number of innings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
