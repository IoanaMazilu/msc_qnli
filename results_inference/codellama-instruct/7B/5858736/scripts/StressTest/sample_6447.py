# define variables with representative names for the numerical entities in both inputs
age_john_premise = 20
age_frank_premise = 10
age_john_hypothesis = 16
age_frank_hypothesis = 8

# extract all quantities as valid numbers (integers or floats)
age_john_premise = int(age_john_premise)
age_frank_premise = int(age_frank_premise)
age_john_hypothesis = int(age_john_hypothesis)
age_frank_hypothesis = int(age_frank_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
if age_john_hypothesis <= age_john_premise * 2:
    # check if the estimate of 'age_john_hypothesis' contradicts the number of years until John is twice as old as Frank
    label = "contradiction"
elif age_frank_hypothesis!= age_frank_premise:
    # check if the number of years until Frank is twice as old as John in the hypothesis contradicts the number of years until Frank is twice as old as John reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
