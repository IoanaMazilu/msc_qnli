premise = "In an exam, Bright scored 60 percent, Bivi scored 65 percent and Lisa 45 percent."
hypothesis = "In an exam, Bright scored more than 60 percent, Bivi scored 65 percent and Lisa 45 percent."

# extract the numerical entities from the premise
premise_entities = re.findall(r'\d+', premise)

# extract the numerical entities from the hypothesis
hypothesis_entities = re.findall(r'\d+', hypothesis)

# check if the hypothesis refers to the same entities as the premise
if premise_entities == hypothesis_entities:
    # check if the hypothesis value contradicts the premise value
    if hypothesis_entities[0] <= premise_entities[0]:
        label = "contradiction"
    else:
        label = "entailment"
else:
    label = "neutral"

print(label)
