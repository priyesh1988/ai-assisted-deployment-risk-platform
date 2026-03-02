
import numpy as np

def extract_features(diff):
    return np.array([
        len(diff.get("files", [])),
        diff.get("lines_added", 0),
        diff.get("lines_removed", 0),
        len(diff.get("dependencies", [])),
        len(diff.get("past_incidents", []))
    ])
