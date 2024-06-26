weeks_premise = 2
weeks_hypothesis = 2

# the hypothesis and premise mention the number of weeks between a controversial study and the response of the ECB
if weeks_hypothesis!= weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the number of weeks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
