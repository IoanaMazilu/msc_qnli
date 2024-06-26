work_days_premise = ["Monday", "Wednesday", "Friday"]
work_days_hypothesis = ["Monday", "Wednesday", "Friday"]

# the hypothesis talks about the number of work days, which is also referred to in the premise
for day in work_days_hypothesis:
    if day not in work_days_premise:
        # if the hypothesis mentions a work day that is not in the premise, it contradicts the premise
        label = "contradiction"
        break

print(label)
