judges_premise = 8
judges_hypothesis = 11

# the hypothesis talks about the number of judges in the Yugoslavia war tribunal, which is also mentioned in the premise
if judges_hypothesis!= judges_premise:
    # check if the number of judges in the hypothesis contradicts the number of judges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
