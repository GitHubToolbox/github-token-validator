<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/GitHubToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/githubtoolbox/black-and-white-circle-256.png" alt="GitHubToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/GitHubToolbox/github-token-validator/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/GitHubToolbox/github-token-validator/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/GitHubToolbox/github-token-validator/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/GitHubToolbox/github-token-validator?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/GitHubToolbox/github-token-validator">
        <img src="https://img.shields.io/github/created-at/GitHubToolbox/github-token-validator?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/GitHubToolbox/github-token-validator/releases/latest">
        <img src="https://img.shields.io/github/v/release/GitHubToolbox/github-token-validator?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/GitHubToolbox/github-token-validator/releases/latest">
        <img src="https://img.shields.io/github/release-date/GitHubToolbox/github-token-validator?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/GitHubToolbox/github-token-validator/releases/latest">
        <img src="https://img.shields.io/github/commits-since/GitHubToolbox/github-token-validator/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/GitHubToolbox/github-token-validator/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GitHubToolbox/github-token-validator/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GitHubToolbox/github-token-validator/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GitHubToolbox/github-token-validator/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

The GitHub Token Validator is a command-line tool that validates a GitHub personal access token and displays its associated information,
such as token scopes, rate limits, and the time remaining until the rate limit reset. This tool helps users to easily check the status
and details of their GitHub tokens.

## Features
- Validate GitHub personal access tokens.
- Display token scopes and rate limit information.
- Show time remaining until the rate limit reset.
- Handle various error scenarios gracefully.

## Installation

```bash
pip install wolfsoftware.github-token-validator
```

## Usage
To run the GitHub Token Validator, use the following command:

```bash
gtv [OPTIONS]
```

### Command-Line Options
- `-h, --help`: Show the help message and exit.
- `-v, --version`: Show the program's version number and exit.
- `-t, --token TOKEN`: Specify the GitHub personal access token. (required)
- `-T, --timeout TIMEOUT`: Specify the request timeout in seconds. (default: 10)

### Example Output

```
+----------------------+-----------------------------+
| Name                 | Value                       |
+----------------------+-----------------------------+
| Token Scope          | read:org, repo, workflow    |
| Rate Limit           | 5000                        |
| Rate Limit Used      | 717                         |
| Rate Limit Remaining | 4283                        |
| Time Till Reset      | 0 hour, 38 minute, 9 second |
+----------------------+-----------------------------+
```

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
