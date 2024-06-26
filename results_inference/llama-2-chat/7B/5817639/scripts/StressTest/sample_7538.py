average_premise = 40 + 60 + 70 + 80 + 80
average_hypothesis = 30 + 40 + 50 + 60 + 70

# the hypothesis talks about the average of grades obtained by Reeya in different subjects
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of the average in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average, and the hypothesis does not contradict it
    label = "entailment"

print(label)
