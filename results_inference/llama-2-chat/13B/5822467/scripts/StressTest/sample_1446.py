deaths_premise = 5
remainder_premise = 15
deaths_hypothesis = 4

# define variables with representative names for the numerical entities in both inputs
deaths_premise_var = 5
remainder_premise_var = 15
deaths_hypothesis_var = 4

# extract all quantities as valid numbers (integers or floats)
deaths_premise_int = int(deaths_premise)
remainder_premise_int = int(remainder_premise)
deaths_hypothesis_int = int(deaths_hypothesis)

# perform calculations if necessary
remainder_hypothesis_int = int(15 * (1 - (deaths_hypothesis_int / 100)))

# compare the variables
if deaths_premise_int <= deaths_hypothesis_int:
    # check if the estimate of 'deaths_hypothesis_int' contradicts the number of deaths in the premise
    label = "contradiction"
elif remainder_hypothesis_int!= remainder_premise_int:
    # check if the number of people who left the village in the hypothesis contradicts the number of people who remained in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
