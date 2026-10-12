# Local Pip Wheel Installer

Automated offline installation tool designed for corporate and restricted network environments.

## Purpose & Target Audience

This tool is created specifically for engineers working within **restricted corporate networks, air-gapped environments, and secure internal perimeters** where direct access to the official Python Package Index (`pypi.org`) is blocked by firewalls or corporate security policies.

### Workflow: Home Machine to Corporate Workstation
\**Download dependencies on an external machine (e.g. Home PC with internet access):**
   Download required binary wheels matching the target OS and Python version directly into the `wheels/` directory:
   ```bash
   pip download -r requirements.txt -d ./wheels --only-binary=:all: --python-version 3.13 --platform win_amd64
