sums_attempted_premise = 80
sums_attempted_hypothesis = 30
marks_obtained_premise = 65
marks_obtained_hypothesis = 65

# the hypothesis refers to the number of sums attempted and marks obtained by Sandy as mentioned in the premise
if sums_attempted_hypothesis >= sums_attempted_premise:
    # check if the number of 'sums_attempted_hypothesis' contradicts the premise of less than 'sums_attempted_premise'
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the marks obtained in the hypothesis contradicts the marks obtained reported in the premise
    label = "contradiction"
else:
    # any number of sums less than 'sums_attempted_premise' and exactly 'marks_obtained_premise' marks is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
