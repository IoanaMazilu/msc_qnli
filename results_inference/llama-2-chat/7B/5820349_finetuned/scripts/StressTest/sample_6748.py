butter_kg_premise = 84
butter_kg_hypothesis = 44

# the hypothesis talks about the amount of butter mixed by Raman, referenced also in the premise
if butter_kg_hypothesis >= butter_kg_premise:
    # check if the hypothesis value contradicts the estimate of less than 'butter_kg_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of butter
    # any amount of butter less than 'butter_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
