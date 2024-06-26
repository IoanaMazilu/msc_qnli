inmates_premise = 200 # "hundreds" is vague but can be interpreted as any number in the hundreds. For a conservative approach, we'll use 200 - the lowest number in the hundreds.
inmates_hypothesis = 200

# the hypothesis mentions the number of escaped inmates, which is also referenced in the premise
# however, the premise does not specify the exact number, only saying "potentially hundreds"
if inmates_hypothesis > inmates_premise:
    # check if the number of inmates in the hypothesis exceeds the possible number from the premise
    label = "contradiction"
else:
    # if the number of inmates from the hypothesis does not exceed the potential number from the premise, it's a neutral relation
    label = "neutral"

print(label)
