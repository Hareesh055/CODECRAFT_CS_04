\# 🛡️ Ethical Keylogger \& Secure Console Auditor

\*\*Task-04: Simple Keylogger\*\*



A Python-based input monitoring utility that bridges the gap between offensive security concepts and defensive auditing requirements. This tool is engineered with a "Security by Design" philosophy, where real-time hardware hooking, automated PII redaction, and efficient resource management of logs are implemented.

---



\## 📋 Project Overview

The project aims to demonstrate the potential of an existing monitoring tool to be leveraged as an ethical keylogger. This project has been implemented to capture user inputs while ensuring compliance with data privacy regulations such as the GDPR by ensuring that sensitive data is never stored in plain text.



\### Key Features

\* \*\*Dual Operating Modes:\*\* \* \*\*Interactive Mode:\*\* Real-time hardware hooks implemented to facilitate local system auditing.

&nbsp;   \* \*\*Simulated Mode:\*\* Console-based inputs to support restricted access and cloud-based auditing.

\* \*\*Redaction of Personally Identifiable Information (PII):\*\* An automated Regex-based system to ensure that any sequence of 12+ digits is replaced with a generic string to prevent credit card information and ID number exposure.

\* \*\*Log Integrity Management:\*\* Utilises the `RotatingFileHandler` to prevent disk exhaustion and the `os.chmod` function to restrict access to the log file.

\* \*\*Consent-Based:\*\* User verification is required before the background monitoring process can be initiated.

---



\## 🏗️ Technical Architecture



\* \*\*Language:\*\* Python 3.10+

\* \*\*Libraries:\*\* `pynput` (Hardware hooks), `logging` (Secure I/O), `re` (Sanitisation).

\* \*\*Security Layer:\*\* Implements file-level permissions (0o600) to ensure only the process owner can access audit logs.



---



\## 🚀 Getting Started



\### Prerequisites

\* Python 3.8+

\* Terminal/Command Prompt access



\### Installation

1\. \*\*Clone the repository:\*\*

&nbsp;  ```bash

&nbsp;  git clone \[https://github.com/Hareesh055/CODECRAFT_CS_04.git](https://github.com/Hareesh055/CODECRAFT_CS_04.git)

&nbsp;  cd CODECRAFT_CS_04



Usage

Execute the main script and follow the interactive prompts:



Bash

python main.py

Note: On Linux systems, hardware hooking may require sudo privileges to access input devices.



\## 🛠️ Testing \& Validation



Scenario  | Input  | Logged Output  | Status  

---------|--------|---------------|--------

Standard Text | """User Login""" | """User Login""" |✅ Pass  

Sensitive Data | """ID: 1234567890123456""" | """ID: \[REDACTED]""" |✅ Pass  

Special Keys | \[Shift] + \[Enter] | """\[Key.shift] \[Key.enter]""" |✅ Pass  



\## 🔍 SOC Analyst Perspective



To implement a defensive security strategy, this tool focuses on important detection vectors such as:



API Monitoring: Detection of unauthorized usage of SetWindowsHookEx on Windows.



File Artifacts: Monitoring of suspicious .log files in /tmp/ or C:\\Users\\Public\\.



Behavioral Analysis: Detection of background Python processes making frequent writes to local storage.



\## ⚖️ Ethical Disclaimer



This project is for educational/authorized purposes only. Any form of unauthorized usage of a keylogger is illegal and unethical. The author of this project does not take responsibility for misuse of the code. Explicit consent must be obtained before usage.

