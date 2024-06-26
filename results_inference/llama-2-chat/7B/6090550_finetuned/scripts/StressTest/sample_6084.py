work_days_premise = 20
work_days_hypothesis = 10

# the hypothesis talks about the number of days it takes for Ram and Shyam to do a piece of work, which is also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
