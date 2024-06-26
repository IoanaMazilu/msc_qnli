england_france_premise = 6
england_france_hypothesis = 8
italy_france_premise = 0
italy_france_hypothesis = 0

# the hypothesis talks about the number of members who traveled to both England and France, referenced also in the premise
if england_france_hypothesis <= england_france_premise:
    # check if the hypothesis value contradicts the estimate of less than 'england_france_premise'
    label = "contradiction"
elif italy_france_hypothesis!= italy_france_premise:
    # check if the number of members who traveled to both Italy and France in the hypothesis contradicts the number of members who traveled to both Italy and France reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members who traveled to both England and France
    # any number of members who traveled to both England and France less than 'england_france_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
