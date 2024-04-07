# Premise: Dawson completes a piece of work in less than 70 days, Rose completes the same work in 60 days.
# Hypothesis: Dawson completes a piece of work in 40 days, Rose completes the same work in 60 days.
# Golden Label: neutral

dawson_work_premise = 70
rose_work_premise = 60
dawson_work_hypothesis = 40
rose_work_hypothesis = 60

# the hypothesis talks about the time taken by Dawson and Rose to complete a piece of work, referenced also in the premise
if dawson_work_hypothesis >= dawson_work_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dawson_work_premise'
    label = "contradiction"
elif rose_work_hypothesis != rose_work_premise:
    # check if the time taken by Rose in the hypothesis contradicts the time taken by Rose reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Dawson
    # any time less than 'dawson_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

