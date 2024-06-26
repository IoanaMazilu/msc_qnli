apples_anita_premise = 460
apples_anita_hypothesis = 360

# the hypothesis talks about the number of apples Anita has, referenced also in the premise
if apples_anita_hypothesis >= apples_anita_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apples_anita_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples less than 'apples_anita_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
