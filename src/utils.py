import subprocess


def run_script(script_path) -> (str, str):
    """
    Runs a script and captures the output or the exception message, if an exception is thrown.
    :param script_path: the path to the script to be run
    :return: the stdout output value of the script or the string "error" if an exception occurs. Also, the exception
    message is returned, or an empty string if no exception occurs.
    """
    try:
        # Run the script using subprocess.run
        result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        label = result.stdout.strip()
        # print(label)
        if label.lower() == "true" or label.lower() == "entailment":
            return "entailment", ""
        elif label.lower() == "false" or label.lower() == "contradiction":
            return "contradiction", ""
        elif label.lower() == "neutral":
            return "neutral", ""
        else:
            return "error", "No output"
    except subprocess.CalledProcessError as e:
        # If an exception is thrown, capture the exception information
        captured_error = e.stderr.strip()
        return "error", captured_error