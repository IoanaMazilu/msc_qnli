# Premise: Sandy attempts 30 sums and obtains 65 marks.
# Hypothesis: Sandy attempts more than 30 sums and obtains 65 marks.
# Golden Label: contradiction

sums_attempted_premise = 30
sums_attempted_hypothesis = 30
marks_obtained_premise = 65
marks_obtained_hypothesis = 65

# the hypothesis talks about the number of sums attempted by Sandy and the marks obtained, referenced also in the premise
if sums_attempted_hypothesis != sums_attempted_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the number of obtained marks in the hypothesis contradicts the number of obtained marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

