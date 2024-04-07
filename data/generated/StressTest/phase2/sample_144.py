# Premise: Andy solves problems 78 to 125 inclusive in a Math exercise.
# Hypothesis: Andy solves problems more than 28 to 125 inclusive in a Math exercise.
# Golden Label: entailment

problems_start_premise = 78
problems_end_premise = 125
problems_start_hypothesis = 28
problems_end_hypothesis = 125

# the hypothesis talks about the number of problems solved by Andy, referenced also in the premise
if problems_start_hypothesis <= problems_start_premise:
    # check if the problems_start_hypothesis contradicts the number of problems_start_premise
    label = "contradiction"
elif problems_end_hypothesis != problems_end_premise:
    # check if the number of problems_end_hypothesis contradicts the number of problems_end_premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

