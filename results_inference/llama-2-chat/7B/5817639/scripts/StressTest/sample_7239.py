father_age_premise = 0 # assume the premise gives the father's age
father_age_hypothesis = 6 # assume the hypothesis gives Ayisha's age

# the hypothesis talks about Ayisha's age, which is also referred to in the premise
if father_age_hypothesis <= father_age_premise:
    # check if the hypothesis value contradicts the estimate of 'father_age_premise'
    label = "contradiction"
elif father_age_hypothesis < 3 * father_age_premise:
    # check if the estimate of 'father_age_hypothesis' is less than 3/6 th of the premise value
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
