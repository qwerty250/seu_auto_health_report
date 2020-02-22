# seu_auto_health_report

# Overview

The script automatically does the daily health report during the 2019-nCOV outbreak so you don't get bugged by *fudaoyuan* all the time.

# Requirements

1. Install Python 3.

2. Install Python language bindings for Selenium WebDriver.
   You can do this by `pip install -U selenium` if you have `pip` too.
   
3. Install corresponding browser driver and add it in PATH.

   Visit https://www.selenium.dev/downloads/ and find your browser in Browsers section. Download the corresponding driver of your browser. Put it in ./webdriver. Add the directory to your PATH. You may need to edit code in case you are not using Chrome. 

4. Edit auto_report.py and replcace the placeholders in Line 1 with your ID card number and password.

# Usage
python auto_report.py and there you go.

A message box is shown whether successful or not.

# Disclaimer

The code is licensed under MIT license.

You assume total responsibility and risk for your use of the script. If you are feeling unwell, stop using the script and report honestly.

