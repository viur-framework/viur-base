from viur.core.render import admin, json, vi
from viur.core import conf, current, config, translate
from . import html
from viur.core.render.html.utils import jinjaGlobalFunction


@jinjaGlobalFunction
def inject_vite(render, development: bool | None = None, development_server: str = "http://localhost:8081"):
    """build vue imports from manifest"""

    if development is None and conf.instance.is_dev_server:
        import logging
        import requests

        try:
            resp = requests.get(development_server, timeout=2)
            development = resp.status_code == 200
        except Exception:
            logging.warning(f"{development_server} isn't active, using prebuilt fallback")
            development = False

    if development:
        return f"""
            <script type="module" src="{development_server}/@vite/client"></script>
            <script type="module" src="{development_server}/main.js"></script>
        """

    import json
    vite_path = "static/site"

    try:
        with open(f"{vite_path}/.vite/manifest.json", "r") as fd:
            manifest = json.load(fd)
    except Exception as e:
        raise Exception(
            f"Vite manifest file not found or invalid {e=}. Maybe your /{vite_path}/.vite/manifest.json file is empty?"
        )

    return f"""
        <script type="module" src="/{vite_path}/{manifest["index.html"]["file"]}"></script>
        <link rel="stylesheet" type="text/css" href="/{vite_path}/{manifest["index.html"]["css"][0]}" />
    """ + "".join(
        f"""<script type="module" src="/{vite_path}/{manifest[file]["file"]}"></script>"""
        for file in (manifest["index.html"].get("imports") or ())
    )
