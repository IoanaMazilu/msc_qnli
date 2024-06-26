total_premise = 8200
total_hypothesis = 4200

# the hypothesis refers to the total amount shared between John, Jose & Binoy, also mentioned in the premise
if total_hypothesis >= total_premise:
    # check if the total amount in the hypothesis contradicts the estimate of less than 'total_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount
    # any total amount less than 'total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
