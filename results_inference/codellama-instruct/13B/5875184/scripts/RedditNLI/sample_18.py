premise = "Sensex closed 362.75 Pts, Tomorrow sure stock future trading call, India best advisory company, Intraday nifty future tips today."
hypothesis = "SENSEX & Nifty down, Sensex down 357.39 Pts, Nifty future tips, Intraday stock future trading call tomorrow, today nifty future call."

# extract the numerical entities from the premise
premise_close = float(premise.split(" ")[0])
premise_tomorrow = float(premise.split(" ")[2])
premise_india = float(premise.split(" ")[4])
premise_intraday = float(premise.split(" ")[6])

# extract the numerical entities from the hypothesis
hypothesis_sensex = float(hypothesis.split(" ")[0])
hypothesis_nifty = float(hypothesis.split(" ")[2])
hypothesis_future = float(hypothesis.split(" ")[4])
hypothesis_tomorrow = float(hypothesis.split(" ")[6])
hypothesis_today = float(hypothesis.split(" ")[8])

# compare the numerical entities between the premise and the hypothesis
if premise_close!= hypothesis_sensex:
    label = "contradiction"
elif premise_tomorrow!= hypothesis_tomorrow:
    label = "contradiction"
elif premise_india!= hypothesis_nifty:
    label = "contradiction"
elif premise_intraday!= hypothesis_future:
    label = "contradiction"
else:
    label = "neutral"

print(label)
