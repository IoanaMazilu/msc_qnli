john_age_in_years_premise = 5
john_age_in_years_hypothesis = 8
frank_age_in_years_premise = 0 # assume Frank's age is 0, since we don't know it
frank_age_in_years_hypothesis = 0 # assume Frank's age is 0, since we don't know it

# the hypothesis refers to John's age in the future, which is also mentioned in the premise
if john_age_in_years_premise <= john_age_in_years_hypothesis:
    # check if the estimate of 'john_age_in_years_hypothesis' contradicts the age of John in the premise
    label = "contradiction"
elif frank_age_in_years_hypothesis!= frank_age_in_years_premise:
    # check if the age of Frank in the hypothesis contradicts the age of Frank reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
