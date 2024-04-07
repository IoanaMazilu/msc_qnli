# Premise: The average of Suresh’s marks in English and History is more than 15.
# Hypothesis: The average of Suresh’s marks in English and History is 55.
# Golden Label: neutral

average_marks_premise = 15
average_marks_hypothesis = 55

# the hypothesis talks about the average mark of Suresh in English and History, also mentioned in the premise
if average_marks_hypothesis <= average_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average mark
    # any number of average marks greater than 'average_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

