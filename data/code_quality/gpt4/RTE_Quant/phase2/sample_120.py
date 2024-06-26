arab_states_premise = 7
arab_states_hypothesis = 7
year_premise = 1948
year_hypothesis = 1948

# the hypothesis talks about the number of Arab states and the year which are also mentioned in the premise
# but the narrative of the two sentences contradict each other
if arab_states_hypothesis != arab_states_premise:
    # check if the number of Arab states in the hypothesis contradicts the number of states from the premise
    label = "contradiction"
elif year_hypothesis != year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, but narrative contradicts
    label = "contradiction"

print(label)
