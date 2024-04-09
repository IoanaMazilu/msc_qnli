# Define variables for the numerical entities in the input sentences
premise_day = 0  # Monday
premise_hours = 0  # hours during which the demonstration takes place
premise_participants = 0  # number of participants in the demonstration
hypothesis_participants = 0  # number of Palestinians permitted to demonstrate

# Extract all quantities as valid numbers (integers or floats)
premise_day = int(premise.split()[0])
premise_hours = int(premise.split()[1])
premise_participants = int(premise.split()[2])
hypothesis_participants = int(hypothesis.split()[0])

# Use brief comments to explain what comparison you do between the defined variables
# (do not use their values in the comments)
# Compare the number of hours during which the demonstration takes place
# (the premise does not mention the number of hours, but the hypothesis does)
if premise_hours!= hypothesis_hours:
    print("contradiction")
# Compare the number of participants in the demonstration
# (the premise does not mention the number of participants, but the hypothesis does)
if premise_participants!= hypothesis_participants:
    print("contradiction")
# Check if the number of Palestinians permitted to demonstrate
# (the hypothesis mentions a specific number, but the premise does not)
if hypothesis_participants!= 0:
    print("entailment")
else:
    print("neutral")
