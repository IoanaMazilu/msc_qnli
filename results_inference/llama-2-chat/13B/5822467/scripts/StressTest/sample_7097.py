nitin_ranks_premise = 15
nitin_ranks_hypothesis = 65

# the hypothesis refers to the rank of Nitin in the class
if nitin_ranks_premise <= nitin_ranks_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif nitin_ranks_hypothesis > 47:
    # check if the hypothesis value contradicts the information that the class has 47 students
    label = "contradiction"
else:
    # if the hypothesis value is consistent with the premise value and the information that the class has 47 students, we can infer neutrality
    label = "neutral"

print(label)
