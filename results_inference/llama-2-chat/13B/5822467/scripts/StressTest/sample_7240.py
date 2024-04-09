ayisha_age_premise = 3/6 * father_age_premise
hypothesis_age = 1/6 * father_age_hypothesis

# the hypothesis refers to Ayisha's age in relation to her father's age
if hypothesis_age <= ayisha_age_premise:
    # check if the hypothesis value contradicts the estimate of Ayisha's age in the premise
    label = "contradiction"
elif ayisha_age_premise!= hypothesis_age:
    # check if the estimate of Ayisha's age in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
