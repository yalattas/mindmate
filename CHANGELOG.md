
# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
## [v0.1.6](#0.1.6) - 2023-06-09 - latest

### Added
- Image command
    - Allowing user to generate an image based on prompt as an input.
    - Save image to the current directory where user called the command.

- Exception handlation
    - Raising exception in few cases to better explain what happened to the user.

- Prompt
    - A generic class to handle user input and `expires_at` as a placeholder.
### Changed
- ai command
    - changed to `directory` to be more descriptive
- user id
    - adding brand name before `uuid` for `openAi` to distinguish users. `uuid` values seems to be similar which make `openAi` confused about context
- config state
    - storing `Prompt` to environment file state without impact existing credentials

### Removed
- openAI model
    - remove unsupported models on `openAi`
- AWS platform - __currently not supported__

> `v0.1.4` and `v0.1.5` wasn't documented and has a problems addressed in `v0.1.6`. Therefore, wasn't tagged

## [v0.1.3](#v0.1.3) - 2023-06-06

### Added
- OpenaiManager
    - This introduces a dedicated sub-module for seamless OpenAI integration, improving modularity and organization of the codebase.
    - supporting stream responses to prompts. This enables real-time access to partial responses as they're being generated.
    - supporting direct prompt and response functionality to openAI

## [v0.0.5](#v0.0.5) - 2023-06-03 - Released - Beta

### Added
- cli version
    - a new command allowing users to fetch current build version number

### Changed
- AI directory
    - all resources are now coming from the cloud, enabling users to get latest updates of directory without the need of upgrading the cli version

## [v0.0.4](#0.0.4) - 2023-06-03 - Not released
- pip didn't include latest code for some reason and build seems to be missing critical parts

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
