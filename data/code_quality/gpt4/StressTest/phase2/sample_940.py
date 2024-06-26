earnings_premise = 858
earnings_hypothesis = 358

# The hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # Check if the earnings value in the hypothesis contradicts the condition of less than 'earnings_premise'
    label = "contradiction"
elif earnings_hypothesis < earnings_premise:
    # If the earnings value in the hypothesis doesn't contradict the condition of less than 'earnings_premise', 
    # then it can be inferred as entailment
    label = "entailment"

print(label)
