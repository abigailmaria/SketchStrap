# test_sketchstrap.py
"""
Tests for SketchStrap module.
"""

import unittest
from sketchstrap import SketchStrap

class TestSketchStrap(unittest.TestCase):
    """Test cases for SketchStrap class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchStrap()
        self.assertIsInstance(instance, SketchStrap)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchStrap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
