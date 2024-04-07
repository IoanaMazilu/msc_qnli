# Premise: If Jos é reads at a constant rate of less than 3 pages every 6 minutes, how many seconds will it take him to read N pages?
# Hypothesis: If Jos é reads at a constant rate of 2 pages every 6 minutes, how many seconds will it take him to read N pages?
# Golden Label: neutral

reading_rate_premise = 3
reading_rate_hypothesis = 2

# the hypothesis refers to the reading rate mentioned in the premise
if reading_rate_hypothesis >= reading_rate_premise:
    # check if the hypothesis rate contradicts the premise's estimate of less than 'reading_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the reading rate
    # a reading rate of 'reading_rate_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

