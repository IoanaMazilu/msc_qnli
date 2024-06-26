cleaning_time_premise = 6
cleaning_time_hypothesis = 5

# the hypothesis talks about the time Jim takes to clean the house, referenced also in the premise
if cleaning_time_hypothesis!= cleaning_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
