# define variables with representative names for the numerical entities in both inputs
interest_premise = 8
interest_hypothesis = 4
amount_premise = 100
amount_hypothesis = 100

# extract all quantities as valid numbers (integers or floats)
interest_premise = float(interest_premise)
interest_hypothesis = float(interest_hypothesis)
amount_premise = float(amount_premise)
amount_hypothesis = float(amount_hypothesis)

# compare the variables
if interest_hypothesis <= interest_premise:
    # check if the estimate of 'interest_hypothesis' contradicts the value of 'interest_premise'
    label = "contradiction"
elif amount_hypothesis!= amount_premise:
    # check if the number of roses in the hypothesis contradicts the number of roses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
