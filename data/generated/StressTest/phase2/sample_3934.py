# Premise: Ravi can do a piece of work in more than 14 days while Prakash can do it in 40 days.
# Hypothesis: Ravi can do a piece of work in 24 days while Prakash can do it in 40 days.
# Golden Label: neutral

work_days_ravi_premise = 14
work_days_ravi_hypothesis = 24
work_days_prakash_premise = 40
work_days_prakash_hypothesis = 40

# the hypothesis refers to the time Ravi and Prakash need for a piece of work, as mentioned in the premise
if work_days_ravi_hypothesis <= work_days_ravi_premise:
    # check if the time Ravi needs in the hypothesis contradicts the estimate of more than 'work_days_ravi_premise' days
    label = "contradiction"
elif work_days_prakash_hypothesis != work_days_prakash_premise:
    # check if the time Prakash needs in the hypothesis contradicts the time Prakash needs reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Ravi needs
    # any time needed by Ravi greater than 'work_days_ravi_premise' days is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

