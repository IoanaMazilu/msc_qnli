# Premise: If Peter reads at a constant rate of 1 pages every 5 minutes, how many seconds will it take him to read N pages?
# Hypothesis: If Peter reads at a constant rate of less than 1 pages every 5 minutes, how many seconds will it take him to read N pages?
# Golden Label: contradiction

reading_rate_premise = 1  # pages per 5 minutes
reading_rate_hypothesis = 1  # pages per 5 minutes

# The hypothesis specifies a reading rate for Peter, which is also mentioned in the premise
if reading_rate_hypothesis >= reading_rate_premise:
    # Check if the hypothesis reading rate contradicts the premise reading rate
    label = "contradiction"
else:
    # The premise gives a specific reading rate for Peter
    # A lower reading rate in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

