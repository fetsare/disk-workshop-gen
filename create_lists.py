import requests
import json
import pandas as pd
import argparse
from datetime import timedelta, date

URL = "https://handledning.dsv.su.se/servlet/teacher/CreateListServlet"


def get_thursdays(start_date, end_date):
    # https://stackoverflow.com/questions/67883300/print-all-thursdays-between-date-range 🙏
    days_to_thursday = (3 - start_date.weekday()) % 7
    week_diff = ((end_date - start_date).days - days_to_thursday) // 7
    return [
        start_date + timedelta(days=days_to_thursday + 7 * more_weeks)
        for more_weeks in range(week_diff + 1)
    ]


def get_dates(start_date_str=None, end_date_str=None):
    if not start_date_str:
        print("Enter start date (YYYY-MM-DD):")
        start_date_str = input().strip()
    start_date = date.fromisoformat(start_date_str)

    if not end_date_str:
        print("Enter end date (YYYY-MM-DD):")
        end_date_str = input().strip()
    end_date = date.fromisoformat(end_date_str)

    return get_thursdays(start_date, end_date)


def main():
    parser = argparse.ArgumentParser(description="Create tutor lists for DISK workshop")
    parser.add_argument(
        "-j", "--jsessionid", required=True, help="JSESSIONID cookie value"
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Dry run, show requests without sending",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose output, show all request details",
    )
    parser.add_argument(
        "-s",
        "--start-date",
        type=str,
        help="Start date (YYYY-MM-DD), will be prompted if not given",
    )
    parser.add_argument(
        "-e",
        "--end-date",
        type=str,
        help="End date (YYYY-MM-DD), will be prompted if not given",
    )

    args = parser.parse_args()

    dates = get_dates(args.start_date, args.end_date)
    if not dates:
        print("No dates found")
        return

    session = requests.Session()
    session.cookies.update({"JSESSIONID": args.jsessionid})

    with open("body.json", "r") as file:
        payload = json.load(file)

    for date in dates:
        payload["listdate"] = date.strftime("%Y-%m-%d")

        if args.dry_run:
            print(f"[DRY RUN] Would send request for date: {date}")
            if args.verbose:
                print(f"URL: {URL}")
                print(f"Payload: {json.dumps(payload, indent=2)}")
            continue

        if args.verbose:
            print(f"Sending request for date: {date}")
            print(f"URL: {URL}")
            print(f"Payload: {json.dumps(payload, indent=2)}")

        response = session.post(URL, data=payload)

        print(f"{date} - Status: {response.status_code}")

        if response.status_code != 200:
            print(f"Response: {response.text}")


if __name__ == "__main__":
    main()
