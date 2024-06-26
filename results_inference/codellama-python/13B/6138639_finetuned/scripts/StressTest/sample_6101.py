days_alone_premise = 16
days_alone_hypothesis = 76

# the hypothesis talks about the number of days Mary will take to complete a task alone, referenced also in the premise
if days_alone_hypothesis!= days_alone_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
