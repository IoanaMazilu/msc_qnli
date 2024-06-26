members_travel_england_france_premise = 8
members_travel_england_france_hypothesis = 6
members_travel_england_italy_premise = 0
members_travel_england_italy_hypothesis = 0
members_travel_france_italy_premise = 11
members_travel_france_italy_hypothesis = 11

# the hypothesis talks about the number of members who traveled to both England and France, no members who traveled to both England and Italy, and members who traveled to both France and Italy
if members_travel_england_france_hypothesis >= members_travel_england_france_premise:
    # check if the hypothesis value contradicts the estimate of less than'members_travel_england_france_premise'
    label = "contradiction"
elif members_travel_england_italy_hypothesis!= members_travel_england_italy_premise:
    # check if the number of members who traveled to both England and Italy in the hypothesis contradicts the number of members who traveled to both England and Italy reported in the premise
    label = "contradiction"
elif members_travel_france_italy_hypothesis!= members_travel_france_italy_premise:
    # check if the number of members who traveled to both France and Italy in the hypothesis contradicts the number of members who traveled to both France and Italy reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members who traveled to both England and France
    # any number of members less than'members_travel_england_france_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
