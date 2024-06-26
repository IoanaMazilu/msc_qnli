england_travelers_premise = 56
france_travelers_premise = 26
italy_travelers_premise = 32

england_travelers_hypothesis = 26
france_travelers_hypothesis = 26
italy_travelers_hypothesis = 32

# the hypothesis talks about the number of travelers to England, France and Italy, referenced also in the premise
if england_travelers_hypothesis >= england_travelers_premise:
    # check if the hypothesis value contradicts the estimate of less than 'england_travelers_premise'
    label = "contradiction"
elif france_travelers_hypothesis!= france_travelers_premise or italy_travelers_hypothesis!= italy_travelers_premise:
    # check if the number of travelers to France or Italy in the hypothesis contradicts the number of travelers to France or Italy reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of travelers to England
    # any number of travelers to England less than 'england_travelers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
