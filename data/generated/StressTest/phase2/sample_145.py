# Premise: Andy solves problems more than 28 to 125 inclusive in a Math exercise.
# Hypothesis: Andy solves problems 78 to 125 inclusive in a Math exercise.
# Golden Label: neutral

problem_start_premise = 28
problem_end_premise = 125
problem_start_hypothesis = 78
problem_end_hypothesis = 125

# the hypothesis talks about the range of problems solved by Andy, referenced also in the premise
if problem_start_hypothesis < problem_start_premise or problem_end_hypothesis > problem_end_premise:
    # check if the hypothesis range contradicts the premise range
    label = "contradiction"
elif problem_start_hypothesis == problem_start_premise and problem_end_hypothesis == problem_end_premise:
    # check if the hypothesis range is exactly the same as the premise range
    label = "entailment"
else:
    # the premise gives a larger range for the problems solved
    # if the hypothesis range is within the premise range, but not exactly the same, it's consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

