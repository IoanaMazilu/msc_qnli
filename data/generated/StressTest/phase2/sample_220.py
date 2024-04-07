# Premise: Sandy attempts less than 70 sums and obtains 60 marks.
# Hypothesis: Sandy attempts 30 sums and obtains 60 marks.
# Golden Label: neutral

sums_attempted_premise = 70
sums_attempted_hypothesis = 30
marks_obtained_premise = 60
marks_obtained_hypothesis = 60

# the hypothesis refers to the number of sums attempted and marks obtained by Sandy, mentioned in the premise
if sums_attempted_hypothesis >= sums_attempted_premise:
    # check if the number of sums attempted in the hypothesis contradicts the estimate of less than 'sums_attempted_premise'
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the number of marks obtained in the hypothesis contradicts the number of marks obtained reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

