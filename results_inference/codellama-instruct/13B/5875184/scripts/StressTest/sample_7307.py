premise_monday = 9
premise_wednesday = 9
premise_friday = 9
premise_tuesday = 5
premise_thursday = 5

hypothesis_monday = 5
hypothesis_wednesday = 5
hypothesis_friday = 5
hypothesis_tuesday = 5
hypothesis_thursday = 5

# check if the hypothesis values contradict the premise values
if hypothesis_monday!= premise_monday or hypothesis_wednesday!= premise_wednesday or hypothesis_friday!= premise_friday:
    label = "contradiction"
elif hypothesis_tuesday!= premise_tuesday or hypothesis_thursday!= premise_thursday:
    label = "contradiction"
else:
    label = "entailment"

print(label)
