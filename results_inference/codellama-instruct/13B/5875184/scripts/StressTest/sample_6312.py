premise = "How many ways are there for 4 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?"
hypothesis = "How many ways are there for more than 2 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?"

# extract the numerical entities from the premise and hypothesis
premise_males = 4
premise_females = 3
hypothesis_males = 2
hypothesis_females = 3

# check if the hypothesis value contradicts the premise value
if hypothesis_males < premise_males:
    label = "contradiction"
elif hypothesis_females < premise_females:
    label = "contradiction"
else:
    label = "neutral"

print(label)
