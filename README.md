# ml-core

Reusable ML utilities library with a flat public API and structured internals.

## Installation

```bash
pip install "ml-core[prefect]"
# or
pip install ml-core
```

## Quickstart

```python
from mlcore import get_logger, read_df, ModelCard

log = get_logger(__name__)
df = read_df("data/examples.csv")
card = ModelCard(name="demo", version="0.1.0", metrics={"auc": 0.88})
log.info({"model_card": card.as_dict()})
```

## Philosophy

- Flat public surface via `from mlcore import ...`
- Structured internals by domain for maintainability
- Optional extras for integrations such as Prefect and S3

## Versioning policy

ml-core follows [Semantic Versioning](https://semver.org/). For pre-1.0
releases, consumers should pin to `<0.2` to avoid breaking changes.

## Deprecations

Deprecated APIs remain available and emit `DeprecationWarning` for at
least one minor release before removal.

## Two-plane workflow

Template repositories depend on this library with an upper bound and are
kept up to date via automation (Renovate, Dependabot, etc.).
