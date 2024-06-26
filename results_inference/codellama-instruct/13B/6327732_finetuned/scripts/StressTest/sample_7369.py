marks_english_premise = 15
marks_history_premise = 15
marks_english_hypothesis = 55
marks_history_hypothesis = 55

# the hypothesis refers to the average of Suresh's marks in English and History
if marks_english_hypothesis <= marks_english_premise and marks_history_hypothesis <= marks_history_premise:
    # check if the estimate of'marks_english_hypothesis' and'marks_history_hypothesis' contradicts the average of marks in English and History in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average of Suresh's marks in English and History
    # any number of marks greater than'marks_english_premise' and'marks_history_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
