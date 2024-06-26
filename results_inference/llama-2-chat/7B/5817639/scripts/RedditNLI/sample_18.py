# Premise
premise_text = "Sensex closed 362.75 Pts, Tomorrow sure stock future trading call, India best advisory company, Intraday nifty future tips today."
premise_entities = {"Sensex": 362.75, "tomorrow": 1, "stock future trading call": 1, "India": 1, "intraday nifty future tips": 1}

# Hypothesis
hypothesis_text = "SENSEX & Nifty down, Sensex down 357.39 Pts, Nifty future tips, Intraday stock future trading call tomorrow, today nifty future call."
hypothesis_entities = {"SENSEX": 357.39, "Nifty": 1, "down": 1, "intraday stock future trading call": 1, "tomorrow": 1, "today nifty future call": 1}

# Comparison
if hypothesis_entities["SENSEX"]!= premise_entities["Sensex"] or hypothesis_entities["Nifty"]!= premise_entities["India"]:
    label = "contradiction"
elif hypothesis_entities["down"] < premise_entities["Sensex"]:
    label = "contradiction"
else:
    label = "entailment"

print(label)
