# Premise: Clinical trials involve 240 patients in 10 centres with each patient questioned three times.
# Hypothesis: Clinical trials involve an average of 200 patients per trial.
# Golden Label: neutral

patients_in_trials_premise = 240
average_patients_per_trial_hypothesis = 200

# the hypothesis talks about the average number of patients involved in clinical trials
# the premise provides specific data about one trial in which 240 patients are involved

if patients_in_trials_premise < average_patients_per_trial_hypothesis:
    # check if the number of patients involved in the clinical trial from the premise is less than the average number of patients per trial in the hypothesis
    label = "contradiction"
elif patients_in_trials_premise > average_patients_per_trial_hypothesis:
    # check if the number of patients involved in the clinical trial from the premise is more than the average number of patients per trial in the hypothesis
    label = "contradiction"
else:
    # if the number of patients involved in the clinical trial from the premise is equal to the average number of patients per trial in the hypothesis
    label = "entailment"

print(label)

