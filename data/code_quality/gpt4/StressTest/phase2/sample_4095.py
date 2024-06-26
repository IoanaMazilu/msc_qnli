sweets_division_premise = (5, 6)
sweets_division_hypothesis = (4, 6)

# in the hypothesis, it is mentioned that Jenny can divide her sweets equally among a certain number of people
# the premise specifies two exact numbers for the equal division, and the hypothesis specifies one exact number and one estimate
if sweets_division_hypothesis[0] >= sweets_division_premise[0] or sweets_division_hypothesis[1] != sweets_division_premise[1]:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif sweets_division_hypothesis[0] < sweets_division_premise[0]:
    # check if the hypothesis value can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise ones and cannot be explicitly entailed from the premise, we can infer neutrality
    label = "neutral"
    
print(label)
