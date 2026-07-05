#!/usr/bin/env python3
"""
TEST RUNNER FOR TRADING BOT
This script executes the trading bot and captures the output for verification.
"""

import subprocess
import sys
import os

def run_bot_test():
    """Execute the trading bot and capture output"""
    print("\n" + "="*80)
    print("🚀 TRADING BOT TEST EXECUTION STARTED")
    print("="*80)
    print(f"Python Version: {sys.version}")
    print(f"Working Directory: {os.getcwd()}")
    print("="*80 + "\n")
    
    try:
        # Run the bot
        result = subprocess.run(
            [sys.executable, "trading_bot_testable.py"],
            capture_output=False,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            print("\n" + "="*80)
            print("✅ BOT EXECUTION COMPLETED SUCCESSFULLY")
            print("="*80)
            return True
        else:
            print("\n" + "="*80)
            print(f"❌ BOT EXECUTION FAILED WITH CODE: {result.returncode}")
            print("="*80)
            return False
    
    except subprocess.TimeoutExpired:
        print("\n" + "="*80)
        print("⏱️  BOT EXECUTION TIMED OUT (> 120 seconds)")
        print("="*80)
        return False
    
    except Exception as e:
        print("\n" + "="*80)
        print(f"❌ ERROR DURING EXECUTION: {str(e)}")
        print("="*80)
        return False


if __name__ == "__main__":
    success = run_bot_test()
    sys.exit(0 if success else 1)
