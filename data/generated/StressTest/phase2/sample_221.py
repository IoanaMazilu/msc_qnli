# Premise: Sandy attempts 30 sums and obtains 60 marks.
# Hypothesis: Sandy attempts 40 sums and obtains 60 marks.
# Golden Label: contradiction

sums_attempted_premise = 30
marks_obtained_premise = 60
sums_attempted_hypothesis = 40
marks_obtained_hypothesis = 60

# the hypothesis refers to the number of sums attempted and the marks obtained by Sandy in the premise
if sums_attempted_premise != sums_attempted_hypothesis:
    # check if the number of sums attempted in the hypothesis contradicts the number of sums attempted in the premise
    label = "contradiction"
elif marks_obtained_premise != marks_obtained_hypothesis:
    # check if the number of marks obtained in the hypothesis contradicts the number of marks obtained in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

