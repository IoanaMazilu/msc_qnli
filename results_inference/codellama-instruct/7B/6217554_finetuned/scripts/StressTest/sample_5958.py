# define variables for the number of members traveling to each destination
england_france_premise = 6
england_italy_premise = 0
france_italy_premise = 11

england_france_hypothesis = 8
england_italy_hypothesis = 0
france_italy_hypothesis = 11

# the hypothesis talks about the number of members traveling to each destination, referenced also in the premise
if england_france_hypothesis >= england_france_premise:
    # check if the hypothesis value contradicts the number of members traveling to England and France in the premise
    label = "contradiction"
elif england_italy_hypothesis!= england_italy_premise:
    # check if the number of members traveling to England and Italy in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
elif france_italy_hypothesis!= france_italy_premise:
    # check if the number of members traveling to France and Italy in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
