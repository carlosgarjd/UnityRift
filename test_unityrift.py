# test_unityrift.py
"""
Tests for UnityRift module.
"""

import unittest
from unityrift import UnityRift

class TestUnityRift(unittest.TestCase):
    """Test cases for UnityRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UnityRift()
        self.assertIsInstance(instance, UnityRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UnityRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
