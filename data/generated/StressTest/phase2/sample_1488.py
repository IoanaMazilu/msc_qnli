# Premise: If Peter reads at a constant rate of 1 pages every 5 minutes, how many seconds will it take him to read N pages?
# Hypothesis: If Peter reads at a constant rate of less than 7 pages every 5 minutes, how many seconds will it take him to read N pages?
# Golden Label: entailment

reading_rate_premise = 1
reading_rate_hypothesis = 7

# the hypothesis refers to the reading rate of Peter mentioned in the premise
if reading_rate_hypothesis <= reading_rate_premise:
    # check if the 'reading_rate_hypothesis' contradicts the reading rate in the premise
    label = "contradiction"
else:
    # the premise gives a specific reading rate for Peter
    # any reading rate less than 'reading_rate_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

