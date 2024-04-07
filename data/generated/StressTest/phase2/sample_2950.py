# Premise: If more than 4 yrs are subtracted from the present age of John & the remainder is divided by 18, then the presentage of his grandson Anup is obtained.
# Hypothesis: If 6 yrs are subtracted from the present age of John & the remainder is divided by 18, then the presentage of his grandson Anup is obtained.
# Golden Label: neutral

subtract_years_premise = 4
subtract_years_hypothesis = 6
divide_by_premise = 18
divide_by_hypothesis = 18

# the hypothesis also refers to the process of obtaining the age of Anup through a calculation based on John's age
if subtract_years_hypothesis < subtract_years_premise:
    # check if the number of years subtracted in the hypothesis contradicts the number of years subtracted mentioned in the premise
    label = "contradiction"
elif divide_by_hypothesis != divide_by_premise:
    # check if the number by which the remainder is divided in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # the premise and the hypothesis provide the same method of calculation, but the number of years subtracted from John's age is different
    # the hypothesis does not contradict the premise, but it can't be explicitly entailed from the premise either
    label = "neutral"

print(label)

