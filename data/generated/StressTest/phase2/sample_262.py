# Premise: Sandy attempts less than 80 sums and obtains 55 marks.
# Hypothesis: Sandy attempts 30 sums and obtains 55 marks.
# Golden Label: neutral

sums_attempted_premise = 80
sums_attempted_hypothesis = 30
marks_obtained_premise = 55
marks_obtained_hypothesis = 55

# the hypothesis refers to the number of sums attempted and marks obtained by Sandy, mentioned in the premise
if sums_attempted_hypothesis >= sums_attempted_premise:
    # check if the number of sums attempted in the hypothesis contradicts the estimate of less than 'sums_attempted_premise'
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the marks obtained in the hypothesis contradicts the marks obtained reported in the premise
    label = "contradiction"
else:
    # the number of sums attempted in the hypothesis is less than 'sums_attempted_premise'
    # and the marks obtained match the premise
    # hence we can infer entailment
    label = "entailment"

print(label)

