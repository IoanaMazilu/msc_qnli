# Premise: Dawson completes a piece of work in 40 days, Rose completes the same work in 60 days.
# Hypothesis: Dawson completes a piece of work in 20 days, Rose completes the same work in 60 days.
# Golden Label: contradiction

dawson_work_days_premise = 40
rose_work_days_premise = 60
dawson_work_days_hypothesis = 20
rose_work_days_hypothesis = 60

# the hypothesis refers to the number of days Dawson and Rose need to complete a piece of work
if dawson_work_days_hypothesis != dawson_work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days Dawson needs in the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days Rose needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

