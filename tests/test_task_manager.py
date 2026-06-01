"""
Tests for core module
"""
import unittest
from unittest.mock import patch

from src.core.task_manager import TaskManager
from src.core.models import Task


class TestTaskManager(unittest.TestCase):
    @patch("src.core.task_manager.save_data")
    @patch("src.core.task_manager.load_data", return_value=[])
    @patch("builtins.print")
    def test_add_task_saves_and_prints_test(self, mock_print, mock_load, mock_save):
        tm = TaskManager()

        tm.add_task("Buy milk")

        self.assertEqual(len(tm._tasks), 1)
        self.assertEqual(tm._tasks[0].description, "Buy milk")
        self.assertFalse(tm._tasks[0].completed)
        mock_save.assert_called_once_with(tm._tasks)
        mock_print.assert_called_once_with("Task added: Buy milk")

    @patch("src.core.task_manager.save_data")
    @patch("src.core.task_manager.load_data", return_value=[Task(1, "Task 1")])
    @patch("builtins.print")
    def test_complete_task_marks_task_completed_test(self, mock_print, mock_load, mock_save):
        tm = TaskManager()

        tm.complete_task(1)

        self.assertTrue(tm._tasks[0].completed)
        mock_save.assert_called_once_with(tm._tasks)
        mock_print.assert_called_once_with("Task completed: Task 1")

    @patch("src.core.task_manager.save_data")
    @patch("src.core.task_manager.load_data", return_value=[Task(1, "Task 1")])
    @patch("builtins.print")
    def test_complete_task_nonexistent_does_not_save_test(self, mock_print, mock_load, mock_save):
        tm = TaskManager()

        tm.complete_task(999)

        self.assertFalse(tm._tasks[0].completed)
        mock_save.assert_not_called()
        mock_print.assert_called_once_with("Task not found: #999")

    @patch("src.core.task_manager.save_data")
    @patch("src.core.task_manager.load_data", return_value=[Task(1, "Task 1")])
    @patch("builtins.print")
    def test_delete_task_removes_task_and_saves_test(self, mock_print, mock_load, mock_save):
        tm = TaskManager()

        tm.delete_task(1)

        self.assertEqual(len(tm._tasks), 0)
        mock_save.assert_called_once_with([])
        mock_print.assert_called_once_with("Task deleted: #1")

    @patch("src.core.task_manager.save_data")
    @patch("src.core.task_manager.load_data", return_value=[Task(1, "Task 1")])
    @patch("builtins.print")
    def test_delete_task_nonexistent_does_not_save_test(self, mock_print, mock_load, mock_save):
        tm = TaskManager()

        tm.delete_task(999)

        self.assertEqual(len(tm._tasks), 1)
        mock_save.assert_not_called()
        mock_print.assert_called_once_with("Task not found: #999")


if __name__ == '__main__':
    unittest.main()
