# Premise: more than 3800 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: 4800 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: neutral

total_premise = 3800
total_hypothesis = 4800

# the hypothesis refers to the total amount among John, Jose & Binoy mentioned in the premise
if total_hypothesis <= total_premise:
    # check if the total amount in the hypothesis contradicts the premise estimate of more than 'total_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount
    # any total greater than 'total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

