## Hashenv

CLI tool for populating envs in secure systems. Built for security and speed.

## Local Setup

### Prerequisites

- Python 3.8 or newer
- Git (optional if you already have the repository locally)

### Install dependencies and package

1. Open a terminal in the repository root:

   ```powershell
   cd C:\Users\chestor\Documents\GitHub\hashenv
   ```

2. Create and activate a virtual environment:

   ```terminal
   python -m venv venv
   venv/Scripts/Activate
   ```

3. Upgrade `pip` and install project dependencies:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

4. Install the package in editable mode:

   ```powershell
   python -m pip install -e .
   ```

### Verify installation

Run the built CLI help to confirm the command is available:

```powershell
hashenv --help
```

## Usage Examples

- Print a quick hello message:

  ```powershell
  hashenv hello
  ```

- Verify the CLI is working:

  ```powershell
  hashenv ping
  ```

- Log in with a token (writes `.env` in the repository root):

  ```powershell
  hashenv login <token>
  ```

- Show repository data using the `--all` option:

  ```powershell
  hashenv show-repository --all
  ```

- Run environment installation logic:

  ```powershell
  hashenv install
  ```

## Project Structure

- `pyproject.toml` - package metadata and dependencies
- `requirements.txt` - development/runtime dependency list
- `src/hashenv/cli.py` - CLI entry point and commands
- `src/helpers/` - helper modules used by the CLI

## Architecture for Hashenv including integration with data server

<img width="671" height="681" alt="hashenv-final-overview drawio" src="https://github.com/user-attachments/assets/baa96c15-eb2e-43b2-8ef4-f12ef6e2a4cb" />

