peanuts_premise = 4
peanuts_hypothesis = 2
additional_peanuts_premise = 12
additional_peanuts_hypothesis = 12

# the hypothesis refers to the number of peanuts in a box and the additional peanuts added
if peanuts_hypothesis!= peanuts_premise + additional_peanuts_hypothesis:
    # check if the number of peanuts in the hypothesis contradicts the number of peanuts reported in the premise
    label = "contradiction"
else:
    # any number of peanuts consistent with the premise is neutral
    label = "neutral"

print(label)
