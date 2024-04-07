# Premise: John completes a piece of work in 320 days, Rose completes the same work in 480 days.
# Hypothesis: John completes a piece of work in more than 320 days, Rose completes the same work in 480 days.
# Golden Label: contradiction

john_work_days_premise = 320
john_work_days_hypothesis = 320
rose_work_days_premise = 480
rose_work_days_hypothesis = 480

# the hypothesis talks about the number of days John and Rose need to complete a piece of work, also mentioned in the premise
if john_work_days_hypothesis > john_work_days_premise:
    # check if the hypothesis value contradicts the number of days John needs in the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the number of days Rose needs in the hypothesis contradicts the number of days Rose needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

