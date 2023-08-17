# Change Log

Categories of Changes: Divide the changes into categories to make the changelog more organized. Common categories include:
- Added: New features or functionalities.
- Changed: Modifications to existing features.
- Deprecated: Features that will be removed in future versions.
- Removed: Features that have been removed.
- Fixed: Bug fixes.
- Security: Security-related changes.


*Table of contents:*
- [Change Log](#change-log)
  - [\[pre-release\] - 2023-08-16](#pre-release---2023-08-16)
    - [Added](#added)
  - [\[1.0.0\] - 2023-08-17](#100---2023-08-17)
    - [Added](#added-1)
    - [Changed](#changed)


## [pre-release] - 2023-08-16

### Added
- understand the basics of LangChain framework
- design prompt for boulder park recommendation based on location, modularized as a function in `langchain_boulder.py`

## [1.0.0] - 2023-08-17

### Added
- designed a prompt to recommend routes at `location` and `difficulty` in a function `get_boulder_tables`
- test run with `streamlit` to build initial UI

### Changed
- refactored both function `get_boulder_tables` and `get_boulder-parks` into static methods in `Class LangchainBoulder`

