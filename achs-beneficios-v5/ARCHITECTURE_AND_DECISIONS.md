# ACHS Beneficios – Version 5 (Playwright + AdonisJS Alignment)

## Why Playwright Instead of Python?

The development stack is fully Node/TypeScript (AdonisJS).
Using Playwright keeps:
- Same runtime (Node.js)
- Same Docker images
- Same CI pipeline
- Same dependency ecosystem

This avoids cross-language complexity.

## Boundary Strategy

Applied ISTQB techniques:
- Boundary Value Analysis
- Equivalence Partitioning
- Critical transitions (14.9999→15, 39.9999→40, 69.9999→70)
- Lower bound (0)
- Upper bound (100)

## Infrastructure Integration

CI Pipeline:
1. npm install
2. npm run test
3. Block merge on failure

AdonisJS + Playwright share:
- Environment variables
- Same HTTP stack
- Same TypeScript configuration

## ML Pipeline Architecture

AdonisJS Calculation API feeds ML forecasting layer.
Playwright ensures contract stability before model retraining.
Monitoring layer compares benefit distributions to detect drift.

## Professional Rationale

Python approach focused on financial determinism.
Playwright approach focuses on infrastructure cohesion.

Final choice respects architectural alignment.