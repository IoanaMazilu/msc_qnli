# define variables for the number of members who traveled to both countries
no_england_france_premise = 0
no_england_france_hypothesis = 0
six_england_italy_premise = 6
six_england_italy_hypothesis = 2
eleven_france_italy_premise = 11
eleven_france_italy_hypothesis = 11

# check if the hypothesis values contradict the premise ones
if no_england_france_hypothesis!= no_england_france_premise:
    label = "contradiction"
elif six_england_italy_hypothesis!= six_england_italy_premise:
    label = "contradiction"
elif eleven_france_italy_hypothesis!= eleven_france_italy_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
