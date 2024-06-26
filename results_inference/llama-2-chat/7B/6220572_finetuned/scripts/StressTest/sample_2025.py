john_age_premise = 3
john_age_hypothesis = 5
tom_age_premise = 6
tom_age_hypothesis = 6

# the hypothesis refers to the age difference between John and Tom mentioned in the premise
if john_age_hypothesis <= john_age_premise:
    # check if the estimate of 'john_age_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
elif tom_age_hypothesis!= tom_age_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
