anita_leaves_premise = 7
indu_leaves_premise = 7

anita_leaves_hypothesis = 10
indu_leaves_hypothesis = 14

# the hypothesis talks about the number of days before the work is finished, referenced also in the premise
if anita_leaves_hypothesis > anita_leaves_premise and indu_leaves_hypothesis > indu_leaves_premise:
    # check if the hypothesis values contradict the number of days mentioned in the premise
    label = "contradiction"
elif anita_leaves_hypothesis == anita_leaves_premise and indu_leaves_hypothesis == indu_leaves_premise:
    # check if the hypothesis values do not contradict the premise values
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
