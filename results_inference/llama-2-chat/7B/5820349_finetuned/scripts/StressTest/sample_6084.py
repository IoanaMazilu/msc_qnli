work_days_premise = 20
work_days_hypothesis = 10

# the hypothesis refers to the number of days Ram and Shyam can finish a piece of work, mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
