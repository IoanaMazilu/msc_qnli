father_age_premise = 0 # assume the premise does not provide a value for this variable
father_age_hypothesis = 80 # assume the hypothesis does not provide a value for this variable
shankar_age_premise = 0 # assume the premise does not provide a value for this variable
shankar_age_hypothesis = 40 # assume the hypothesis does not provide a value for this variable

# the hypothesis talks about Ayisha's father's age being twice Shankar's age after a certain time
if father_age_hypothesis <= father_age_premise:
    # check if the hypothesis value contradicts the estimate of 'father_age_premise'
    label = "contradiction"
elif shankar_age_hypothesis!= shankar_age_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
