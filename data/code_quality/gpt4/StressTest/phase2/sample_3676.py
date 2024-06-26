birthday_premise = 43
birthday_hypothesis = 23
birth_year = 1950
celebration_year = 2016

# the hypothesis talks about the age of James in 2016, also referenced in the premise
if birthday_hypothesis >= birthday_premise:
    # check if the age in the hypothesis contradicts the estimate of less than 'birthday_premise'
    label = "contradiction"
else:
    # calculate the real age of James in 2016
    real_age = celebration_year - birth_year
    if birthday_hypothesis != real_age:
        # check if the age in the hypothesis contradicts the real age of James
        label = "contradiction"
    else:
        # if the hypothesis age does not contradict the estimate in the premise and matches the real age,
        # we can infer entailment
        label = "entailment"

print(label)
