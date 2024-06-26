members_traveled_england_france_premise = 6
members_traveled_england_france_hypothesis = 8
members_traveled_england_italy_premise = 0
members_traveled_england_italy_hypothesis = 0
members_traveled_france_italy_premise = 11
members_traveled_france_italy_hypothesis = 11

# the hypothesis talks about the number of members who traveled to both England and France, referenced also in the premise
if members_traveled_england_france_hypothesis >= members_traveled_england_france_premise:
    # check if the hypothesis value contradicts the estimate of less than'members_traveled_england_france_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members who traveled to both England and France
    # any number of members less than'members_traveled_england_france_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
