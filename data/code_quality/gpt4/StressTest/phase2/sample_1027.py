equal_parts_premise = 1
equal_parts_hypothesis = 5
six_parts_premise = 6
six_parts_hypothesis = 6
nine_parts_premise = 9
nine_parts_hypothesis = 9

# the hypothesis talks about the ability to divide the herd into equal parts, referenced also in the premise
if equal_parts_hypothesis <= equal_parts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'equal_parts_premise'
    label = "contradiction"
elif six_parts_hypothesis != six_parts_premise:
    # check if the number of divisions in the hypothesis contradicts the number of divisions reported in the premise
    label = "contradiction"
elif nine_parts_hypothesis != nine_parts_premise:
    # check if the number of divisions in the hypothesis contradicts the number of divisions reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of divisions 
    # any number of divisions greater than 'equal_parts_premise' and not equal to 'nine_parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
