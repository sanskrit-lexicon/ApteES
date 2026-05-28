# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ApteES** is a Sanskrit dictionary digitization and corrections repository in the Sanskrit Lexicon project.

## Architecture

| Directory | Purpose |
|---|---|
| (root) | Main dictionary source and correction files |

## Common Commands

For corrections, see the [GitHub Issue Conventions](#github-issue-conventions) section below.

## GitHub Issue Conventions

This repository uses a unified issue taxonomy managed via the Cologne Issue Runbook. All issues must have exactly one type label, one severity label, and one milestone.

### Issue Types (exactly one per issue)
- **link-target**: Building click-throughs from citations to scanned pages
- **link-splitting**: Splitting combined references into individual links
- **markup**: Normalizing XML tag content
- **text-correction**: Corrections to German/English definitions or headwords
- **content-enhancement**: New material and structural additions
- **encoding**: SLP1/IAST/Devanagari transcoding
- **scan-quality**: Replacing blurry, skewed, or missing scan pages
- **bug**: Broken links, XML errors, download issues
- **question**: Scholarly questions requiring research

### Severity (exactly one per issue)
- **minor**: Targeted fix (handful of lines or single file)
- **medium**: Standard unit of work (one index, batch of corrections)
- **hard**: Large effort spanning many sources/files/dictionaries

### Milestones
- **Dictionary to Book**: link-target, link-splitting issues
- **Digitization Quality**: scan-quality, encoding, bug, text-correction issues
- **Structured Data**: markup, question issues
- **Major Enhancements**: content-enhancement issues

## Dependencies

- Python 3
- GitHub CLI (`gh`)
