# Premise: No there is not a $2 TRILLION error in the budget.
# Hypothesis: Trump Budget Based on $2 Trillion Math Error.
# Golden Label: contradiction

error_premise = 2
error_hypothesis = 2

# the hypothesis and premise mention a $2 TRILLION error in the budget
if error_hypothesis != error_premise:
    # check if the error amount in the hypothesis contradicts the error amount in the premise
    label = "contradiction"
else:
    # if the error amount in the hypothesis and premise match, it's a contradiction because the premise denies the existence of the error while the hypothesis asserts it
    label = "contradiction"

print(label)

