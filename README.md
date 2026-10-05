# BINGO HAVEL – Website

Statische Website (HTML, CSS, JavaScript) für https://www.bingohavel.com. Kein Build-Schritt, keine Abhängigkeiten, kein Webflow nötig.

## Aufbau

- `docs/` – die veröffentlichte Website
  - `index.html`, `about.html`, `work.html`, `project-index.html`
  - `work/<projekt>.html` – die Projektseiten
  - `assets/` – Bilder, Schriften, CSS und JavaScript
  - `CNAME` – verbindet die Domain mit GitHub Pages (nicht ändern)
- `preview.py` – lokale Vorschau: `python3 preview.py`, dann http://127.0.0.1:4173 öffnen

## Veröffentlichen

Hosting über GitHub Pages: Repository `bingohavel/bingohavel.github.io`, Branch `main`, Ordner `/docs`. Änderungen in GitHub Desktop committen und mit „Push origin“ hochladen. Nach etwa einer Minute sind sie live.

Das Repository ist öffentlich: Unveröffentlichte Inhalte gehören nicht in diesen Ordner, sondern nach `../00 DRAFTS`.

## Neues Projekt

Material liegt in `../02 WORK/<projekt>/` (Work Hero, Project Media, Project Info.txt). Daraus werden `docs/work/<projekt>.html` und die Kachel in `docs/work.html` erstellt.

Die Git-Versionsgeschichte liegt nicht in diesem Ordner, sondern lokal unter `~/.local/share/bingohavel-website/git`. Die Datei `.git` hier verweist darauf und darf nicht gelöscht werden.
