# Premise: If Packard reads at a constant rate of more than 1 pages every 5 minutes, how many seconds will it take him to read N pages?
# Hypothesis: If Packard reads at a constant rate of 4 pages every 5 minutes, how many seconds will it take him to read N pages?
# Golden Label: neutral

reading_rate_premise = 1
reading_rate_hypothesis = 4

# the hypothesis talks about the reading rate of Packard, referenced also in the premise
if reading_rate_hypothesis <= reading_rate_premise:
    # check if the hypothesis rate contradicts the estimate of more than 'reading_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the reading rate
    # any rate greater than 'reading_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

