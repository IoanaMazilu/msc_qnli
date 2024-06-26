killed_premise = 4
wounded_premise = 'several' # not a specific number
wounded_hypothesis = 10

# the hypothesis mentions the number of people wounded, which is also referenced in the premise
# but the exact number of people wounded in the premise is not specified, only that there are 'several'
if wounded_hypothesis <= killed_premise:
    # check if the number of people wounded in the hypothesis contradicts the number of people killed in the premise
    label = "contradiction"
else:
    # if the number of people wounded in the hypothesis does not contradict the number of people killed in the premise
    # we can infer a neutral relation since 'several' does not necessarily mean less than 10
    label = "neutral"

print(label)
