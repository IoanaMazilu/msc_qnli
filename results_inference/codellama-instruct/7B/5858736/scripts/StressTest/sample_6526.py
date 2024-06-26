premise_on_time_rate = 20
hypothesis_on_time_rate = 60

if premise_on_time_rate <= hypothesis_on_time_rate:
    label = "contradiction"
else:
    label = "entailment"

print(label)
