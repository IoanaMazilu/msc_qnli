years_future = 6
years_present = 4
age_future = 38
age_present = 38

# the hypothesis refers to the same situation as the premise, but with a different time frame
if years_future > years_present:
    # check if the future age is greater than the present age, which is not possible according to the premise
    label = "contradiction"
elif age_future!= age_present:
    # check if the future age is different from the present age, which is not possible according to the premise
    label = "contradiction"
else:
    # if the hypothesis and premise values do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
