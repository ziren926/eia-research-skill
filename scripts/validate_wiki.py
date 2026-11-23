"""Validate the portable EIA source and document indexes."""

import json
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1] / "skills/eia-research/references/wiki"
OFFICIAL_SUFFIXES = (".gov.cn", ".cnemc.cn")


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def check(condition, message):
    if not condition:
        raise ValueError(message)


def ids(items, label):
    values = [item["id"] for item in items]
    check(len(values) == len(set(values)), f"duplicate {label} ID")
    return set(values)


def official_url(value):
    parsed = urlsplit(value)
    host = parsed.hostname or ""
    return (
        parsed.scheme == "https"
        and not parsed.username
        and not parsed.password
        and (host.endswith(OFFICIAL_SUFFIXES) or host == "cnemc.cn")
    )


def valid_date(value):
    if value is not None:
        date.fromisoformat(value)


def main():
    catalog = load("catalog.json")
    documents = load("documents.json")
    modules = ids(catalog["modules"], "module")
    sources = ids(catalog["sources"], "source")
    ids(documents["records"], "document")
    valid_date(catalog["checked_on"])
    valid_date(documents["recorded_on"])

    for module in catalog["modules"]:
        check(bool(module["source_ids"]), f"{module['id']}: no sources")
        check(set(module["source_ids"]) <= sources, f"{module['id']}: unknown source")
    for source in catalog["sources"]:
        check(official_url(source["url"]), f"{source['id']}: invalid official URL")
        valid_date(source["checked_on"])
    for record in documents["records"]:
        check(bool(record["module_ids"]), f"{record['id']}: no modules")
        check(set(record["module_ids"]) <= modules, f"{record['id']}: unknown module")
        check(record["source_id"] in sources, f"{record['id']}: unknown source")
        check(official_url(record["landing_url"]), f"{record['id']}: invalid official URL")
        check(isinstance(record["full_text_reviewed"], bool), f"{record['id']}: invalid review status")
        for field in ("page_date", "effective_on", "link_checked_on"):
            valid_date(record[field])
        for attachment in record["attachments"]:
            check(official_url(attachment["url"]), f"{record['id']}: invalid attachment URL")
        if record["kind"] == "consultation_draft":
            check(record["effective_on"] is None, f"{record['id']}: draft has effective date")

    print(f"OK: {len(modules)} modules, {len(sources)} sources, {len(documents['records'])} documents")


if __name__ == "__main__":
    main()
