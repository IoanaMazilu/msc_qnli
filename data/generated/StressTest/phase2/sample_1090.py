# Premise: Matthew's walking rate was less than 8 km per hour and Johnny's was 4 km per hour, how many km had Johnny walked when they met?
# Hypothesis: Matthew's walking rate was 3 km per hour and Johnny's was 4 km per hour, how many km had Johnny walked when they met?
# Golden Label: neutral

matthew_rate_premise = 8
johnny_rate_premise = 4
matthew_rate_hypothesis = 3
johnny_rate_hypothesis = 4

# The hypothesis talks about Matthew's and Johnny's walking rate, which is also referenced in the premise
if matthew_rate_hypothesis >= matthew_rate_premise:
    # Check if the hypothesized walking rate for Matthew contradicts the premise's estimate of less than 'matthew_rate_premise'
    label = "contradiction"
elif johnny_rate_hypothesis != johnny_rate_premise:
    # Check if the hypothesized walking rate for Johnny contradicts the exact walking rate for Johnny given in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

