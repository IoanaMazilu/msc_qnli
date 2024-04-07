# Premise: If they do n't die for any reason James can make new farm in 6 years with baby goat and older goats.
# Hypothesis: If they do n't die for any reason James can make new farm in less than 7 years with baby goat and older goats.
# Golden Label: entailment

farm_years_premise = 6
farm_years_hypothesis = 7

# the hypothesis refers to the years needed to set up a new farm mentioned in the premise
if farm_years_hypothesis < farm_years_premise:
    # check if the estimate of 'farm_years_hypothesis' contradicts the number of years mentioned in the premise
    label = "contradiction"
elif farm_years_premise != farm_years_hypothesis:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

