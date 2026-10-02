# Bingo Havel

Migration der 22 öffentlich erreichbaren Seiten von https://www.bingohavel.com, Stand 28.09.2026. Die Original-HTML-Struktur, CSS-Regeln, Interaktionen und 492 Assets liegen lokal unter `docs/`. Enthalten sind Bilder, responsive Bildvarianten, GIFs, Videos, Schriftdateien, Icons und JavaScript.

Die Seite benötigt weder einen Webflow-Account noch Webflow-Hosting, um ausgeliefert zu werden. Zur originalgetreuen Wiedergabe bleiben die lokal gespeicherten, von Webflow erzeugten CSS- und JavaScript-Dateien erhalten. Die frühere Webflow-Analytics-Proxy-Einbindung wurde entfernt. Externe redaktionelle Links bleiben erhalten.

## Bearbeiten

Inhalte können direkt in den HTML-Dateien unter `docs/` geändert werden. Gemeinsame Styles und die ursprünglichen Interaktionsskripte befinden sich unter `docs/assets/`. Für weitere Änderungen kann ChatGPT dieses Projekt bearbeiten. Es gibt keine Abhängigkeiten zu installieren und keinen Build-Schritt.

## Hosting

Als statische Website aus `docs/` ausliefern. Der Host muss HTML-Dateien auch unter ihren ursprünglichen Adressen ohne `.html` bedienen (z. B. `/about`, `/project-index`, `/work/freizeitwelt`). Die Sites-Projektzuordnung steht in `.openai/hosting.json`.

## Umfang und Grenzen

Erfasst wurden Sitemap und interne Links. Nicht veröffentlichte Webflow-Entwürfe, CMS-Verwaltung, Versionshistorie und Kontoeinstellungen sind über die öffentliche Website nicht zugänglich. Die bestehende Domain und der Webflow-Vertrag wurden nicht verändert. Vor der Domainumstellung sollte die Kopie nochmals mit dem Original abgeglichen werden; eine vollständige Pixelgleichheit sämtlicher Zustände ist nicht nachgewiesen.
