sums_attempted_premise = 30
sums_attempted_hypothesis = 70
marks_obtained_premise = 60
marks_obtained_hypothesis = 60

# the hypothesis talks about the number of sums attempted and marks obtained by Sandy, referenced also in the premise
if sums_attempted_hypothesis < sums_attempted_premise:
    # check if the hypothesis value contradicts the number of sums attempted in the premise
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the number of marks obtained in the hypothesis contradicts the number of marks obtained in the premise
    label = "contradiction"
elif sums_attempted_hypothesis > sums_attempted_premise:
    # the premise gives a specific number of sums attempted and marks obtained
    # any number of sums attempted less than 'sums_attempted_hypothesis' and exactly 'marks_obtained_hypothesis' marks obtained is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
