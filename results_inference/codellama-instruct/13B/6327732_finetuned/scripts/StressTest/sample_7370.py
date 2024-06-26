marks_english_premise = 55
marks_history_premise = 55
marks_english_hypothesis = 35
marks_history_hypothesis = 35

# the hypothesis refers to the average of Suresh's marks in English and History
if marks_english_hypothesis + marks_history_hypothesis!= marks_english_premise + marks_history_premise:
    # check if the hypothesis value contradicts the premise values
    label = "contradiction"
else:
    # the premise gives the average of Suresh's marks in English and History
    # any average of marks greater than'marks_english_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)