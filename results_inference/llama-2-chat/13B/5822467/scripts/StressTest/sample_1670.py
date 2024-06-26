deaths_premise = 5
remainder_premise = 15
deaths_hypothesis = 10

# define variables with representative names for the numerical entities in both inputs
deaths_premise_var = "deaths_premise"
remainder_premise_var = "remainder_premise"
deaths_hypothesis_var = "deaths_hypothesis"

# extract all quantities as valid numbers (integers or floats)
deaths_premise_num = int(deaths_premise)
remainder_premise_num = int(remainder_premise)
deaths_hypothesis_num = int(deaths_hypothesis)

# compare the variables
if deaths_hypothesis_num > deaths_premise_num:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif deaths_hypothesis_num == deaths_premise_num:
    # check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # check if the hypothesis value entails the premise value
    label = "entailment"

# use the variables to perform calculations if necessary
if deaths_hypothesis_num > deaths_premise_num:
    # calculate the percentage increase in deaths
    percentage_increase = (deaths_hypothesis_num - deaths_premise_num) / deaths_premise_num * 100
    print(f"The percentage increase in deaths is {percentage_increase:.2f}%")

print(label)
