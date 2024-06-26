pencils_premise = 55
pencils_hypothesis = 75
distributed_pencils_premise = 20
distributed_pencils_hypothesis = 20

# the hypothesis refers to the number of pencils John has and number of pencils he distributed
# which are also mentioned in the premise
if pencils_hypothesis <= pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the estimate of more than 'pencils_premise'
    label = "contradiction"
elif distributed_pencils_hypothesis != distributed_pencils_premise:
    # check if the number of distributed pencils in the hypothesis contradicts the number of distributed pencils reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pencils
    # the number 'pencils_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
