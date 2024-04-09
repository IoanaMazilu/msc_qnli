jobs_premise = int(5000)
percentage_premise = 5

hypothesis = "Intel to cut workforce by 5 percent in 2014."

# extract the numerical information from the premise and hypothesis
jobs_hypothesis = int(5000 * 0.05)

# compare the numerical information
if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif jobs_hypothesis < percentage_premise:
    # check if the estimated percentage of the workforce to be cut in the hypothesis contradicts the premise estimate of more than 'percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the workforce to be cut
    # any estimate of the percentage in the hypothesis greater or equal to 'percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
