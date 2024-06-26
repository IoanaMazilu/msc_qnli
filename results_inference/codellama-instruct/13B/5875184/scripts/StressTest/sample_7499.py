premise_age = 34
hypothesis_age = 44
baby_sitting_years = 10

# the hypothesis refers to the age of Jane and the number of years she stopped baby-sitting
if hypothesis_age <= premise_age:
    # check if the estimate of 'hypothesis_age' contradicts the age of Jane in the premise
    label = "contradiction"
elif baby_sitting_years!= 10:
    # check if the number of years she stopped baby-sitting in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
