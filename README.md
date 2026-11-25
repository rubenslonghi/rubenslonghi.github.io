# Matematica in costruzione — sito MyST

Libro multimediale per 1 SP e 2BS. Contenuti in cartelle per capitolo, indice esplicito in myst.yml, esercizi in sottosezioni e soluzioni in direttive dropdown prive di opzione open.

## Compilare

Richiede Node 22 e MyST Markdown 1.10.1: `npm install -g mystmd@1.10.1`, quindi `myst build --html --strict`. L'output per GitHub Pages è `_build/html`. Per l'anteprima locale: `myst start`.

Gli allegati sono in materiali/, media/ e archivio/. Sono copiati come file statici con URL stabili. Le figure SVG sono già compilate e non richiedono TeX sul server. Nessun PDF o foglio di calcolo è una voce autonoma del TOC.

La configurazione di pubblicazione usa il ramo master. Il ramo archivio/pre-libro-2026-11-25 conserva il sito precedente; gli archivi ZIP consentono di scaricarne sorgenti e HTML. Non caricare registri di ricognizione privati o dati degli studenti.
