age_Arun_premise = 5
age_Arun_hypothesis = 2

# the hypothesis talks about the age of Arun after more than 2 years
if age_Arun_hypothesis <= age_Arun_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_Arun_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Arun
    # any number of years greater than 'age_Arun_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
