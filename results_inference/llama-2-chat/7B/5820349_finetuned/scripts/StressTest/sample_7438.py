fastest_horses_premise = 4
fastest_horses_hypothesis = 3
total_horses_premise = 25
total_horses_hypothesis = 25

# the hypothesis talks about the number of fastest horses and total horses, referenced also in the premise
if fastest_horses_hypothesis >= fastest_horses_premise:
    # check if the number of fastest horses in the hypothesis contradicts the estimate of less than 'fastest_horses_premise'
    label = "contradiction"
elif total_horses_hypothesis!= total_horses_premise:
    # check if the total number of horses in the hypothesis contradicts the total number of horses reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fastest horses
    # any number of fastest horses less than 'fastest_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
