import os 
import sys
import csv
import random
import time
import datetime
from common.selenium import Selenium

def main():
    try:
        print(f'===== script start: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} =====')
        selenium = Selenium()
        selenium.sample_function()
        print(f'===== script end: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} =====')
    except Exception as e:
        print(f'Unknown Exception in sample.py: {e}')
    finally:
        # Close Driver
        selenium.driver_quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)