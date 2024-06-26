# define variables with representative names for the numerical entities in both inputs
john_age_premise = 3 * tom_age_premise
john_age_hypothesis = 3 * tom_age_hypothesis

# extract all quantities as valid numbers (integers or floats)
john_age_premise = int(john_age_premise)
john_age_hypothesis = int(john_age_hypothesis)
tom_age_premise = int(tom_age_premise)

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments

# compare the premise and hypothesis values
if john_age_premise <= john_age_hypothesis:
    # check if the estimate of 'john_age_hypothesis' contradicts the value of 'john_age_premise'
    label = "contradiction"
elif tom_age_premise!= tom_age_hypothesis:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
