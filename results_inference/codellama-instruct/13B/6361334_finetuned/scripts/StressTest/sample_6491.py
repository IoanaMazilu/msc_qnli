borrowed_premise = 6500
borrowed_hypothesis = 1500

# the hypothesis refers to the amount borrowed annually for college education, which is also mentioned in the premise
if borrowed_hypothesis <= borrowed_premise:
    # check if the estimate of 'borrowed_hypothesis' contradicts the amount borrowed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount borrowed
    # any amount greater than 'borrowed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
