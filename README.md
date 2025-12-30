# DISK Workshop Tutor List Generator

A tool for automatically creating tutoring lists for DISK Workshop sessions on DSV's tutoring system.

The program automatically generates tutoring lists for all Thursdays within a given date range by sending POST requests to DSV's tutoring system. This simplifies the process of planning regular workshop sessions.

## Author

- [Fredrik Etsare](https://github.com/fetsare)

## Installation

### 1. Clone the project

```bash
git clone https://github.com/fetsare/disk-workshop-gen.git
cd disk-workshop-gen
```

### 2. Create virtual Python environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**macOS/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic usage

The program requires a JSESSIONID from your logged-in session on the tutoring system:

```bash
python create_lists.py -j "YOUR_JSESSIONID_HERE"
```

You will then be prompted to enter start and end dates.

### With dates as arguments

```bash
python create_lists.py -j "YOUR_JSESSIONID_HERE" -s "2026-01-01" -e "2026-06-30"
```

### Dry run (show what would be sent)

```bash
python create_lists.py -j "YOUR_JSESSIONID_HERE" -s "2026-01-01" -e "2026-06-30" -d
```

### Verbose output (show detailed information)

```bash
python create_lists.py -j "YOUR_JSESSIONID_HERE" -s "2026-01-01" -e "2026-06-30" -v
```

### Combine flags

```bash
python create_lists.py -j "YOUR_JSESSIONID_HERE" -s "2026-01-01" -e "2026-06-30" -d -v
```

## Flags

- `-j, --jsessionid` - **(Required)** JSESSIONID from your logged-in session
- `-s, --start-date` - Start date (YYYY-MM-DD), will be prompted if not provided
- `-e, --end-date` - End date (YYYY-MM-DD), will be prompted if not provided
- `-d, --dry-run` - Run in dry-run mode (shows what would be sent without actually sending)
- `-v, --verbose` - Show detailed information about all requests

## How do I get my JSESSIONID?

1. Log in to the tutoring system in your web browser
2. Open Developer Tools (F12)
3. Go to the "Application" tab (Chrome) or "Storage" tab (Firefox)
4. Under "Cookies" you will find the JSESSIONID value
5. Copy the value and use it with the `-j` flag

## Files

- `create_lists.py` - Main program
- `body.json` - Request payload for the tutoring system
- `requirements.txt` - Python dependencies

## Future development

- Add functionality to add DISK worksop administrator to every new list, curretly this needs to be done manually.
- Create executables with PyInstaller and github actions workflow for new releases

## Disclamer

This is a private project that is not affiliated with or maintained by Stockholm University. It was created to simplify the planning of DISK Workshop sessions.
