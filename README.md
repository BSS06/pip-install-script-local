# Local Pip Wheel Installer

Automated offline installation tool for Python dependencies on Windows x64 systems.

## Overview

This repository provides an automated offline installer for Python environments. It includes pre-packaged binary wheel distributions specifically compiled for Python 3.13 on 64-bit Windows architectures, removing the need for internet access or Microsoft Visual C++ Build Tools during deployment.

## Repository Structure

```text
pip-install-script-local/
├── pip/
│   └── pip.ini
├── wheels/
│   ├── chardet-7.6.0-cp313-cp313-win_amd64.whl
│   ├── et_xmlfile-2.0.0-py3-none-any.whl
│   ├── greenlet-3.5.6-cp313-cp313-win_amd64.whl
│   ├── mathlib-0.6.0-py3-none-any.whl
│   └── numpy-2.5.3-cp313-cp313-win_amd64.whl
├── install.py
└── README.md
