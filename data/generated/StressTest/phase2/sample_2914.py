# Premise: Sandy attempts more than 10 sums and obtains 45 marks.
# Hypothesis: Sandy attempts 30 sums and obtains 45 marks.
# Golden Label: neutral

sums_attempted_premise = 10
sums_attempted_hypothesis = 30
marks_obtained_premise = 45
marks_obtained_hypothesis = 45

# The hypothesis refers to the number of sums attempted and marks obtained by Sandy, which are also mentioned in the premise
if sums_attempted_hypothesis <= sums_attempted_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'sums_attempted_premise'
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # Check if the number of marks obtained in the hypothesis contradicts the number of marks obtained reported in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of sums attempted
    # Any number of sums attempted greater than 'sums_attempted_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

