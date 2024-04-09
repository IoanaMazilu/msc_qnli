unit_digits_premise = 8
unit_digits_hypothesis = 4

# define variables for the numerical entities in the premise and hypothesis
unit_digits_premise_sum = 0
unit_digits_hypothesis_sum = 0

# extract all quantities as valid numbers
unit_digits_premise_list = [digit for digit in str(unit_digits_premise)]
unit_digits_hypothesis_list = [digit for digit in str(unit_digits_hypothesis)]

# perform calculations
unit_digits_premise_sum = sum(unit_digits_premise_list)
unit_digits_hypothesis_sum = sum(unit_digits_hypothesis_list)

# compare the variables
if unit_digits_premise_sum <= unit_digits_hypothesis_sum:
    # check if the estimate of 'unit_digits_hypothesis_sum' contradicts the sum of the unit digits in the premise
    label = "contradiction"
elif unit_digits_hypothesis_sum!= unit_digits_premise_sum:
    # check if the sum of the unit digits in the hypothesis contradicts the sum of the unit digits in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
