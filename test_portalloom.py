# test_portalloom.py
"""
Tests for PortalLoom module.
"""

import unittest
from portalloom import PortalLoom

class TestPortalLoom(unittest.TestCase):
    """Test cases for PortalLoom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortalLoom()
        self.assertIsInstance(instance, PortalLoom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortalLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
