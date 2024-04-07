# Premise: If Jos é reads at a constant rate of 5 pages every 5 minutes, how many seconds will it take him to read N pages?
# Hypothesis: If Jos é reads at a constant rate of less than 7 pages every 5 minutes, how many seconds will it take him to read N pages?
# Golden Label: entailment

reading_rate_premise = 5
reading_rate_hypothesis = 7

# the hypothesis refers to the reading rate mentioned in the premise
if reading_rate_hypothesis <= reading_rate_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise, but also cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

