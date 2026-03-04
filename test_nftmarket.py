# test_nftmarket.py
"""
Tests for NFTMarket module.
"""

import unittest
from nftmarket import NFTMarket

class TestNFTMarket(unittest.TestCase):
    """Test cases for NFTMarket class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTMarket()
        self.assertIsInstance(instance, NFTMarket)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTMarket()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
