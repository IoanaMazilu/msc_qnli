ramesh_work_premise = 60
ramesh_work_hypothesis = 20
sushil_work_premise = 25
sushil_work_hypothesis = 25

# the hypothesis talks about the time Ramesh and Sushil need to finish a work, referenced also in the premise
if ramesh_work_hypothesis >= ramesh_work_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ramesh_work_premise'
    label = "contradiction"
elif sushil_work_hypothesis!= sushil_work_premise:
    # check if the time Sushil needs to finish a work in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Ramesh needs to finish a work
    # any time less than 'ramesh_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
