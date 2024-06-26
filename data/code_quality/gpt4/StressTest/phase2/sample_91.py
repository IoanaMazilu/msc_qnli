old_john_premise = 3
old_tom_premise = old_john_premise/3

old_john_hypothesis = 6
old_tom_hypothesis = old_john_hypothesis/3

# the hypothesis talks about John and Tom's age difference, referenced also in the premise
if old_john_hypothesis != old_john_premise:
    # check if the number of years back in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
elif old_tom_hypothesis != old_tom_premise:
    # check if the age of Tom in the hypothesis contradicts the age of Tom in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
