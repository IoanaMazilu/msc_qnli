years_back_premise = 6
years_back_hypothesis = 1

# the hypothesis refers to the time when John was thrice as old as Tom mentioned in the premise
if years_back_hypothesis >= years_back_premise:
    # check if the 'years_back_hypothesis' contradicts the time stated in the premise
    label = "contradiction"
elif years_back_hypothesis < years_back_premise:
    # any time less than 'years_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
