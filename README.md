# sgfixedincome_cache

This repository serves as a data cache for the [sgfixedincome_pkg python package](https://github.com/GidTay/sgfixedincome_pkg)'s streamlit app (access the app [here](https://sgfixedincome.streamlit.app/)).

This repository is used by the SGFixedIncome Streamlit app to:

1. Load cached data instead of making direct API calls and web scrapes each time the app is opened. This reduces the frequency of direct API calls and web scraping.
2. Fall back to the latest successful version if the current version has failures.

Just in case, the app offers direct data fetching if the cache is more than 2 days old. This should never happen if this repo works as expected.

## Purpose

A simple cache system:

1. Stores the latest scraped data from various Singapore fixed income sources:
    - Scrapes of banks' fixed deposit websites, and
    - Monetary Authority of Singapore's (MAS) API endpoints related to T-bills and Singapore Savings Bonds (SSBs)
2. Maintains both the most recent version and the latest successful version (if different from the most recent version)
    - 'Successful' version is where there is no failed data fetching from MAS's API or any of the default banks websites to scrape from.
3. Updates automatically every 24 hours via GitHub Actions

## Repository Structure
The repository structure is:

```
sgfixedincome_cache/
├── .github/
│   └── workflows/
│       └── update-cache.yml    # GitHub Action workflow
├── scripts/
│   └── update_cache.py        # Cache update script
└── cache/
    ├── metadata.json          # Cache metadata
    ├── data_current.json      # Most recent data
    └── data_latest_successful.json  # Latest successful fetch (if different from current)
```

## Cache System Details

**Data Files**
- `data_current.json`: Always contains the most recent version of the data
- `data_latest_successful.json`: Only exists if the current version has fetch failures
- `metadata.json`: Contains metadata about the cached versions

**Update Schedule**
- The cache automatically updates daily at 00:00 UTC via GitHub Actions
- Manual updates can be triggered from the Actions tab in this repository

**Timestamps**

All timestamps in the cache are in Singapore timezone (UTC+8)

## License

`sgfixedincome_cache` was created by [Gideon Tay](https://github.com/GidTay). It is licensed under the terms of the MIT license.