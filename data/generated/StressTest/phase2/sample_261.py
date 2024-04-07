# Premise: Sandy attempts 30 sums and obtains 55 marks.
# Hypothesis: Sandy attempts less than 80 sums and obtains 55 marks.
# Golden Label: entailment

sums_attempted_premise = 30
sums_attempted_hypothesis = 80
marks_obtained_premise = 55
marks_obtained_hypothesis = 55

# the hypothesis refers to the number of sums attempted and marks obtained by Sandy, mentioned also in the premise
if sums_attempted_hypothesis <= sums_attempted_premise:
    # check if the hypothesis estimate contradicts the number of sums attempted in the premise
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the number of marks obtained in the hypothesis contradicts the number of marks obtained reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

