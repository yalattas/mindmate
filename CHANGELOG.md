
# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [v0.0.3](#v0.0.3) - 2023-04-26 - Released - Alpha

### Hotfix
- [bug: making call without credentials](#8)
    - System was throwing error in case user didn't provide credentials and attempts to submit a prompt, fixed by validating credentials first on utility layer

## [v0.0.2](#v0.0.2) - 2023-04-26 - Released - Alpha

### Added
- [ai command](#6)
    - Allowing users to list available AI platforms based on pre-defined categories
### Changed
- [configure command](#7)
    - checking `--model` value based on selected `--platform` value
    - calling `openai` text completion endpoint to retrieve text -> UNCOOKED
    - handling authentication and RateLimit exceptions

## [v0.0.1](#v0.0.1) - 2023-04-24 - Released - Alpha

### Added
- [configure command](#1)
    - basic functionality to store the value into `yaml file`
