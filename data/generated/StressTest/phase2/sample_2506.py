# Premise: more than 3320 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: 4320 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: neutral

total_premise = 3320
total_hypothesis = 4320

# the hypothesis refers to the total number and ratio of John, Jose & Binoy mentioned in the premise
if total_hypothesis <= total_premise:
    # check if the total number in the hypothesis contradicts the premise's estimate of more than 'total_premise'
    label = "contradiction"
else:
    # the premise gives only a lower boundary for the total number
    # any total number greater than 'total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

