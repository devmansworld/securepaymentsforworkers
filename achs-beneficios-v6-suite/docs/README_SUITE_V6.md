# ACHS Beneficios – Version 6 Modular Suite

## Features

- Modular Playwright test structure
- HTML reporting enabled
- GitHub Actions CI ready
- GitLab CI ready
- Environment configurable via BASE_URL

## Run locally

npm install
npx playwright install
npm run test
npm run report

## CI/CD

Push to main branch triggers automatic execution.
HTML report available as artifact (can be configured).

## Architecture

AdonisJS API
    ↓
Playwright Modular Suite
    ↓
HTML Report
    ↓
CI/CD Gatekeeper