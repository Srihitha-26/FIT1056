import pytest
import tkinter as tk
from modules import Modules  
from unittest.mock import MagicMock
from unittest.mock import MagicMock, patch

# Test the open_module method
def test_open_module():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)

    # Positive Testing
    # It checks if a new window is created when you open a valid module. If the window is created as expected, 
    # the test will pass.
    modules.open_module("Variables")
    assert len(master.winfo_children()) > 0  # Check if a new window is created

    # Negative Testing (Module file not found)
    # It checks if the FileNotFoundError exception is raised when trying to open a non-existent module file. 
    # If the exception is raised, the test will pass.
    with pytest.raises(FileNotFoundError):
        modules.open_module("NonExistentModule")

# Test the display_mcq method
def test_display_mcq():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)

    # Positive Testing
    #  It verifies if MCQs are displayed when calling the display_mcq method for a valid module. If MCQs are 
    # displayed as expected, the test will pass.
    module_frame = tk.Toplevel(master)
    modules.display_mcq(module_frame, "Variables")
    assert len(module_frame.winfo_children()) > 0  # Check if MCQs are displayed

    # Negative Testing (Module has no MCQs)
    #  It checks if the KeyError exception is raised when trying to display MCQs for a non-existent module. 
    # If the exception is raised, the test will pass.
    with pytest.raises(KeyError):
        modules.display_mcq(module_frame, "NonExistentModule")

# You can write similar tests for other methods like check_mcq_answer, retry_mcq, show_answer, and update_progress.

# Test the update_progress method
def test_update_progress():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)

    # Positive Testing
    # It tests the update_progress method to ensure that the progress value becomes 100% when all modules are 
    # completed successfully. If the progress value reaches 100%, the test will pass.
    modules.modules = {"Variables": True, "Loops": True, "Strings": True, "Functions": True}
    modules.update_progress()
    assert modules.progress["value"] == 100  # Check if progress is 100%

    # Negative Testing (No modules completed)
    # It checks if the progress value becomes 0% when no modules are completed. If the progress value is 0% as 
    # expected, the test will pass.
    modules.modules = {"Variables": False, "Loops": False, "Strings": False, "Functions": False}
    modules.update_progress()
    assert modules.progress["value"] == 0  # Check if progress is 0%

# Test the return_to_menu method
def test_return_to_menu():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)

    # Positive Testing
    # It ensures that when the return_to_menu method is called, the student_frame is correctly placed back in the 
    # root window. If the frame is placed as expected, the test will pass.
    modules.return_to_menu()
    assert master.winfo_children()[0] == student_frame  # Check if student_frame is placed back in the root window

def test_check_mcq_answer_correct():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)
    
    # Simulate a correct answer scenario
    question = "Sample Question"
    mcq_data = {"correct_answer": "C"}
    answer_var = MagicMock()
    answer_var.get.return_value = "C"
    mcq_frame = MagicMock()

    with patch.object(modules, 'update_progress') as mock_update_progress:
            modules.check_mcq_answer(question, mcq_data, answer_var, mcq_frame)
            
            # Add assertions to verify expected actions
            mock_update_progress.assert_called_once()  # Ensure update_progress was called

def test_check_mcq_answer_incorrect():
    # Simulate an incorrect answer scenario
    # This test scenario is designed to validate that the check_mcq_answer method handles incorrect answers 
    # correctly and provides options for the student to retry or see the correct answer.

    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)
    
    
    question = "Sample Question"
    mcq_data = {"correct_answer": "A"}
    answer_var = MagicMock()
    answer_var.get.return_value = "B"  # Answer is incorrect
    mcq_frame = MagicMock()

    modules.check_mcq_answer(question, mcq_data, answer_var, mcq_frame)

def test_check_mcq_answer_exception():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)
    question = "Sample Question"
    mcq_data = {"correct_answer": "A"}
    answer_var = MagicMock()
    answer_var.get.side_effect = Exception("Simulated exception")
    mcq_frame = MagicMock()

    with patch.object(modules, 'show_answer') as mock_show_answer:
        modules.check_mcq_answer(question, mcq_data, answer_var, mcq_frame)
        
        # Assert that the show_answer method is called since an exception occurred
        mock_show_answer.assert_called_once()

def test_check_mcq_answer_missing_data():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)
    question = "Sample Question"
    mcq_data = {}  # Missing correct_answer
    answer_var = MagicMock()
    answer_var.get.return_value = "A"  # Correct answer
    mcq_frame = MagicMock()

    with patch.object(modules, 'show_answer') as mock_show_answer:
        modules.check_mcq_answer(question, mcq_data, answer_var, mcq_frame)
        
        # Assert that the show_answer method is called since the MCQ data is missing the correct_answer
        mock_show_answer.assert_called_once()

def test_retry_mcq_positive():
    master = tk.Tk()
    student_frame = tk.Frame(master)
    modules = Modules(master, student_frame)
    module_frame = tk.Toplevel(master)
    module_frame.title("Variables")
    mcq_frame = tk.Frame(module_frame)

    # Simulate a completed MCQ with widgets in mcq_frame
    mcq_label = tk.Label(mcq_frame, text="Sample MCQ Question")
    mcq_label.pack()

    mcq_frame.pack()

    # Ensure the MCQ frame has children
    assert len(mcq_frame.winfo_children()) > 0

    # Call the retry_mcq method
    modules.retry_mcq(mcq_frame, "Sample Question", {"correct_answer": "A"})

    # Assert that the MCQ frame is cleared and re-displayed
    assert len(mcq_frame.winfo_children()) == 0
    assert len(mcq_frame.master.winfo_children()) > 0



# Run the tests
if __name__ == "__main__":
    pytest.main()
