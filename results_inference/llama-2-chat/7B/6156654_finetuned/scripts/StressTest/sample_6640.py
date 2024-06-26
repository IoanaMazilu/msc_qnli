work_days_ram_krish = 20
work_days_ram_krish_hypothesis = 40
work_days_bhim = 0

# the hypothesis refers to the work days needed by Ram and Krish to complete the same work, which is also mentioned in the premise
if work_days_ram_krish_hypothesis!= work_days_ram_krish:
    # check if the number of work days in the hypothesis contradicts the number of work days mentioned in the premise
    label = "contradiction"
elif work_days_bhim!= 0:
    # check if Bhim's work days are mentioned in the premise
    label = "neutral"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
