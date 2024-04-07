# Premise: Evan ran a mile in 10 minutes Monday morning, and he ran the same mile in 8 minutes on Tuesday morning.
# Hypothesis: Evan ran a mile in less than 40 minutes Monday morning, and he ran the same mile in 8 minutes on Tuesday morning.
# Golden Label: entailment

monday_run_time_premise = 10
monday_run_time_hypothesis = 40
tuesday_run_time_premise = 8
tuesday_run_time_hypothesis = 8

# Both the hypothesis and premise discuss Evan's run times on Monday and Tuesday
if monday_run_time_premise > monday_run_time_hypothesis:
    # Check if the premise contradicts the hypothesis's claim about Monday's run time
    label = "contradiction"
elif tuesday_run_time_premise != tuesday_run_time_hypothesis:
    # Check if the premise contradicts the hypothesis's claim about Tuesday's run time
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
