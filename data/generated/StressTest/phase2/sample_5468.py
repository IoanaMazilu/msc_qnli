# Premise: His assets included:Investments, ($305,000), Life Insurance ($104,000), an old car (sold for $1900), an older house (sold for $75,000)
# Hypothesis: His assets included:Investments, ($305,000), Life Insurance ($104,000), an old car (sold for $less than 1900), an older house (sold for $75,000)
# Golden Label: contradiction

investments_premise = 305000
life_insurance_premise = 104000
old_car_premise = 1900
older_house_premise = 75000

investments_hypothesis = 305000
life_insurance_hypothesis = 104000
old_car_hypothesis = 1900
older_house_hypothesis = 75000

# The hypothesis values completely match up with the premise values except for the old car price
if investments_hypothesis != investments_premise:
    # Check if the investment value presented in the hypothesis contradicts the premise
    label = "contradiction"
elif life_insurance_hypothesis != life_insurance_premise:
    # Check if the life insurance value presented in the hypothesis contradicts the premise
    label = "contradiction"
elif old_car_hypothesis > old_car_premise:
    # Check if the old car price value presented in the hypothesis contradicts the premise
    label = "contradiction"
elif older_house_hypothesis != older_house_premise:
    # Check if the older house price value presented in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

