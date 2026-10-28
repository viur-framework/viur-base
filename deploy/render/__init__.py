from viur.core.render import admin, html, json, vi
from viur.core import conf, current, config, translate
from viur.core.render.html.utils import jinjaGlobalFunction


@jinjaGlobalFunction
def inject_vite(
    render: html.default,
    development: bool | None = None,
    development_server: str = "http://localhost:8081",
    entry: str = "src/main.js",
) -> str:
    """build vue imports from the vite manifest"""
    import json
    import logging

    if development is None and conf.instance.is_dev_server:
        import requests

        # autodetect whether the local vite dev server of this site is alive;
        # vite answers unknown paths with its index.html (status 200), so check for actual JavaScript
        try:
            resp = requests.get(f"{development_server}/{entry}", timeout=2)
            development = resp.ok and "javascript" in resp.headers.get("Content-Type", "")
        except Exception:
            logging.warning(f"{development_server} isn't active, using prebuilt fallback")
            development = False
    elif development is None:
        development = False

    if development:
        return "\n".join((
            f'<script type="module" src="{development_server}/@vite/client"></script>',
            f'<script type="module" src="{development_server}/{entry}"></script>',
        ))

    vite_path = "static/site"
    version_suffix = f"?_v={conf.instance.version_hash}"
    manifest_file = conf.instance.project_base_path / vite_path / ".vite" / "manifest.json"

    try:
        with open(manifest_file, "r") as fd:
            manifest = json.load(fd)
    except (FileNotFoundError, ValueError) as exc:
        logging.error(
            f"Vite manifest not found or invalid at {manifest_file}. "
            f"Maybe your {vite_path}/.vite/manifest.json is empty? {exc=}"
        )
        return "<!-- vite manifest not found or invalid -->"

    entry = manifest["index.html"]
    tags = [
        f'<script type="module" src="/{vite_path}/{manifest[file]["file"]}"></script>'
        for file in entry.get("imports") or ()
    ]
    tags.append(
        f'<script type="module" src="/{vite_path}/{entry["file"]}{version_suffix}"></script>'
    )
    tags += [
        f'<link rel="stylesheet" type="text/css" href="/{vite_path}/{css}{version_suffix}">'
        for css in entry.get("css") or ()
    ]
    return "\n".join(tags)
