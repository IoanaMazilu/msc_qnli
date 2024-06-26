monday_run_time_premise = 40
monday_run_time_hypothesis = 10
tuesday_run_time_premise = 8
tuesday_run_time_hypothesis = 8

# The hypothesis refers to the run time of Evan on Monday and Tuesday mornings.

if monday_run_time_hypothesis >= monday_run_time_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'monday_run_time_premise'
    label = "contradiction"
elif tuesday_run_time_hypothesis != tuesday_run_time_premise:
    # Check if the run time on Tuesday in the hypothesis contradicts the run time on Tuesday reported in the premise
    label = "contradiction"
else:
    # The premise provides an estimate for the run time on Monday and a precise time for Tuesday.
    # If the hypothesis times do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
