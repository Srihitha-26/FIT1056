import pytest
import tkinter as tk
from modules import Modules  
from unittest.mock import MagicMock
from unittest.mock import MagicMock, patch

def test_retry_mcq_positive():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)
    module_frame = tk.Toplevel(master)
    module_frame.title("Variables")

    mcq_frame = tk.Frame(module_frame)
    mcq_frame.pack()  # Use pack here

    # Simulate a completed MCQ with widgets in mcq_frame
    mcq_label = tk.Label(mcq_frame, text="Sample MCQ Question")
    mcq_label.pack()

    # Ensure the MCQ frame has children
    assert len(mcq_frame.winfo_children()) > 0

    # Call the retry_mcq method
    modules.retry_mcq(mcq_frame, "Sample Question", {"correct_answer": "A"})

    # Assert that the MCQ frame is cleared and re-displayed
    assert len(mcq_frame.winfo_children()) == 0
    assert len(mcq_frame.master.winfo_children()) > 0

def test_retry_mcq_negative():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)
    mcq_frame = tk.Frame(master)

    # Call the retry_mcq method with an empty frame
    modules.retry_mcq(mcq_frame, "Sample Question", {"correct_answer": "A"})

    # Assert that the MCQ frame remains empty
    assert len(mcq_frame.winfo_children()) == 0




# Run the tests
if __name__ == "__main__":
    pytest.main()
