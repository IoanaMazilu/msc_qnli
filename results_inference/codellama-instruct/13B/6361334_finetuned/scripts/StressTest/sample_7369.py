marks_english_premise = 15
marks_history_premise = 15
marks_english_hypothesis = 55
marks_history_hypothesis = 55

# the hypothesis refers to the average of Suresh's marks in English and History, which is also mentioned in the premise
if marks_english_hypothesis <= marks_english_premise:
    # check if the estimate of'marks_english_hypothesis' contradicts the average of marks in English in the premise
    label = "contradiction"
elif marks_history_hypothesis <= marks_history_premise:
    # check if the estimate of'marks_history_hypothesis' contradicts the average of marks in History in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
