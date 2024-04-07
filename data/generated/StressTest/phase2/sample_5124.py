# Premise: Dawson completes a piece of work in 40 days, Rose completes the same work in 60 days.
# Hypothesis: Dawson completes a piece of work in less than 70 days, Rose completes the same work in 60 days.
# Golden Label: entailment

dawson_work_days_premise = 40
dawson_work_days_hypothesis = 70
rose_work_days_premise = 60
rose_work_days_hypothesis = 60

# the hypothesis refers to the number of days Dawson and Rose need to complete a piece of work, mentioned in the premise
if dawson_work_days_premise >= dawson_work_days_hypothesis:
    # check if the estimate of 'dawson_work_days_hypothesis' contradicts the number of days Dawson needs in the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the number of days Rose needs in the hypothesis contradicts the number of days Rose needs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

