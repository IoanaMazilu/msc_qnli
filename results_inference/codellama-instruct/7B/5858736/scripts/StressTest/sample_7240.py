age_ayisha_premise = 3/6
age_ayisha_hypothesis = 1/6
father_age_premise = 3/6
father_age_hypothesis = 1/6

# the hypothesis talks about Ayisha's age, referenced also in the premise
if age_ayisha_hypothesis <= age_ayisha_premise:
    # check if the hypothesis value contradicts the estimate of less than 'age_ayisha_premise'
    label = "contradiction"
elif father_age_hypothesis!= father_age_premise:
    # check if the father's age in the hypothesis contradicts the father's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
