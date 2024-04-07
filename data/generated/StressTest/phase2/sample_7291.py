# Premise: more than 500 and Greg's share is Rs.
# Hypothesis: 600 and Greg's share is Rs.
# Golden Label: neutral

total_premise = 500
total_hypothesis = 600

# The hypothesis refers to the total amount mentioned in the premise
if total_hypothesis <= total_premise:
    # Check if the total amount in the hypothesis contradicts the estimate of more than 'total_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the total amount
    # any amount greater than 'total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

