ram_shyam_work_premise = 20
ram_shyam_work_hypothesis = 10

# the hypothesis talks about the time it takes to complete a piece of work, referenced also in the premise
if ram_shyam_work_hypothesis <= ram_shyam_work_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ram_shyam_work_premise' days
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes to complete the work
    # any time less than 'ram_shyam_work_premise' days is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
