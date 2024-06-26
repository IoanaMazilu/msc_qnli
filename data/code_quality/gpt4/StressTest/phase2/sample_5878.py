sums_attempted_premise = 10
sums_attempted_hypothesis = 30
marks_obtained_premise = 50
marks_obtained_hypothesis = 50

# the hypothesis talks about the number of sums attempted by Sandy and the marks obtained, both referenced in the premise
if sums_attempted_hypothesis <= sums_attempted_premise:
    # check if the hypothesis value contradicts the estimate of more than 'sums_attempted_premise'
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the marks obtained in the hypothesis contradict the marks obtained reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of sums attempted
    # any number of sums greater than 'sums_attempted_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
