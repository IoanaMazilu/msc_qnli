raman_mix_premise = 27
raman_mix_hypothesis = 47

# the hypothesis talks about the amount of butter mixed by Raman, referenced also in the premise
if raman_mix_hypothesis <= raman_mix_premise:
    # check if the hypothesis value contradicts the estimate of more than 'raman_mix_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of butter
    # any amount of butter greater than 'raman_mix_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
