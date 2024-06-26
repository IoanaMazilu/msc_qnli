age_Arun_premise = 26
age_Arun_hypothesis = 26

# the hypothesis talks about the age of Arun, referenced also in the premise
if age_Arun_hypothesis <= age_Arun_premise:
    # check if the hypothesis value contradicts the estimate of 'age_Arun_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Arun's age
    # any number of years greater than 'age_Arun_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
