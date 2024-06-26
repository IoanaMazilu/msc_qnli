graduate_level_premise = 15
graduate_level_hypothesis = 15

# the hypothesis refers to the percentage of sales staff with a level of graduation mentioned in the premise
if graduate_level_hypothesis!= graduate_level_premise:
    # check if the hypothesis value contradicts the percentage of sales staff with a level of graduation in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of sales staff with a level of graduation
    # any percentage of sales staff with a level of graduation greater than 'graduate_level_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
