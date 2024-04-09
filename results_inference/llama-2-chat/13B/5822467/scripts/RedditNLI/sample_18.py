premise = "Sensex closed 362.75 Pts, Tomorrow sure stock future trading call, India best advisory company, Intraday nifty future tips today."
hypothesis = "SENSEX & Nifty down, Sensex down 357.39 Pts, Nifty future tips, Intraday stock future trading call tomorrow, today nifty future call."

# Define variables with representative names for the numerical entities in both inputs
sensex_premise = 362.75
nifty_premise = None

sensex_hypothesis = 357.39
nifty_hypothesis = None

# Extract all quantities as valid numbers (integers or floats)
# Do not ignore any quantity or numerical information

# Compare the variables

# Check if the sensex in the hypothesis contradicts the sensex in the premise
if sensex_hypothesis!= sensex_premise:
    label = "contradiction"
elif nifty_hypothesis is None or nifty_premise is None:
    # If the hypothesis or premise does not mention nifty, we cannot compare them
    label = "neutral"
else:
    # Check if the nifty in the hypothesis contradicts the nifty in the premise
    label = "neutral"

print(label)
