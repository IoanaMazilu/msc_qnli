# Premise: It will take 18 days for Cameron to complete a certain task alone.
# Hypothesis: It will take less than 18 days for Cameron to complete a certain task alone.
# Golden Label: contradiction

completion_time_premise = 18
completion_time_hypothesis = 18

# the hypothesis talks about the completion time for Cameron to complete a task, referenced also in the premise
if completion_time_hypothesis < completion_time_premise:
    # check if the hypothesis value contradicts the exact time of 'completion_time_premise'
    label = "entailment"
else:
    # if the hypothesis value is equal or more than the premise value, it contradicts the premise
    label = "contradiction"

print(label)

