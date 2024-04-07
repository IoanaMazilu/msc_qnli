# Premise: Sandy attempts 30 sums and obtains 45 marks.
# Hypothesis: Sandy attempts more than 10 sums and obtains 45 marks.
# Golden Label: entailment

sums_attempted_premise = 30
sums_attempted_hypothesis = 10
marks_obtained_premise = 45
marks_obtained_hypothesis = 45

# the hypothesis refers to the number of sums attempted and the marks obtained by Sandy mentioned in the premise
if sums_attempted_premise <= sums_attempted_hypothesis:
    # check if the number 'sums_attempted_hypothesis' contradicts the number of sums attempted in the premise
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the number of marks obtained in the hypothesis contradicts the number of marks obtained reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
