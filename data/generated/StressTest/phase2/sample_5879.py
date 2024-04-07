# Premise: Sandy attempts 30 sums and obtains 50 marks.
# Hypothesis: Sandy attempts more than 30 sums and obtains 50 marks.
# Golden Label: contradiction

sums_attempted_premise = 30
sums_attempted_hypothesis = 30
marks_obtained_premise = 50
marks_obtained_hypothesis = 50

# the hypothesis refers to the number of sums attempted and marks obtained by Sandy mentioned in the premise
if sums_attempted_hypothesis <= sums_attempted_premise:
    # check if the hypothesis value contradicts the exact number of sums attempted mentioned in the premise
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the marks obtained in the hypothesis contradicts the marks obtained reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

