dosaxin_premise = 545
dosaxin_hypothesis = 145

# the hypothesis talks about the amount of Dosaxin given to each patient, referenced also in the premise
if dosaxin_hypothesis >= dosaxin_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dosaxin_premise'
    label = "contradiction"
elif dosaxin_hypothesis < dosaxin_premise:
    # the premise gives only an estimate for the amount of Dosaxin
    # any amount of Dosaxin less than 'dosaxin_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"
else:
    label = "neutral"

print(label)
