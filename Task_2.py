import numpy as np
import time  # Add this import statement for the time module

def reduced_histogram(h, ifirst, ilast):
    """Creates a new histogram in a reduced (zoomed-in) range.

    Args:
        h (np.ndarray): The original histogram.
        ifirst (int): The starting index for the reduced range (inclusive).
        ilast (int): The ending index for the reduced range (exclusive).

    Returns:
        np.ndarray: The reduced histogram.

    Raises:
        ValueError: If ifirst or ilast is outside the valid range of h.
    """

    if ifirst < 0 or ifirst > h.shape[0]:
        raise ValueError("ifirst is out of bounds")

    if ilast < 0 or ilast > h.shape[0]:
        raise ValueError("ilast is out of bounds")

    if ifirst >= ilast:
        return np.array([])  # Return an empty array if the range is empty

    return h[ifirst:ilast]

def print_reduced_histogram_and_sleep(h, ifirst, ilast, sleep_duration):
    """Prints the reduced histogram and sleeps for the specified duration.

    Args:
        h (np.ndarray): The original histogram.
        ifirst (int): The starting index for the reduced range (inclusive).
        ilast (int): The ending index for the reduced range (exclusive).
        sleep_duration (int): The duration to sleep in seconds after printing the histogram.
    """

    reduced_h = reduced_histogram(h, ifirst, ilast)

    print("Reduced Histogram:")
    print(reduced_h)

    time.sleep(sleep_duration)

# Example usage
if __name__ == "__main__":
    h = np.random.rand(100)
    print_reduced_histogram_and_sleep(h, 10, 20, 5)  # Sleep for 5 seconds after printing the reduced histogram
