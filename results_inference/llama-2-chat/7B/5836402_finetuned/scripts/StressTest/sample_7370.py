english_history_average_premise = 55
english_history_average_hypothesis = 35

# the hypothesis talks about the average of Suresh's marks in English and History, referenced also in the premise
if english_history_average_hypothesis!= english_history_average_premise:
    # check if the average in the hypothesis contradicts the average in the premise
    label = "contradiction"
else:
    # if the average in the hypothesis does not contradict the average in the premise, we can infer entailment
    label = "entailment"

print(label)
