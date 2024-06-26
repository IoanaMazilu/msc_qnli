total_premise = 2600
total_hypothesis = 6600

# the hypothesis refers to the total amount among John, Jose & Binoy, mentioned in the premise
if total_hypothesis <= total_premise:
    # check if the total value in the hypothesis contradicts the premise's estimate of more than 'total_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount
    # any total value greater than 'total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
