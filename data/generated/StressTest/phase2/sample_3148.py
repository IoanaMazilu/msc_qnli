# Premise: If Ros é reads at a constant rate of more than 1 pages every 5 minutes, how many seconds will it take her to read N pages?
# Hypothesis: If Ros é reads at a constant rate of 3 pages every 5 minutes, how many seconds will it take her to read N pages?
# Golden Label: neutral

reading_rate_premise = 1
reading_rate_hypothesis = 3

# the hypothesis refers to the reading rate of Ros é, also mentioned in the premise
if reading_rate_hypothesis <= reading_rate_premise:
    # check if the hypothesis reading rate contradicts the premise estimate of more than 'reading_rate_premise'
    label = "contradiction"
else:
    # the premise provides only an estimate for the reading rate
    # any reading rate greater than 'reading_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

