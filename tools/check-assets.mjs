import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const list=JSON.parse(fs.readFileSync('manifest-materiali.json','utf8'));
for(const f of list){const p=path.join('_build/html',f.url);if(!fs.existsSync(p))throw new Error(`Allegato assente: ${f.url}`);const bytes=fs.readFileSync(p);if(crypto.createHash('sha256').update(bytes).digest('hex')!==f.sha256)throw new Error(`Allegato diverso dall'originale: ${f.url}`);}
for(const p of ['archivio/sito-precedente-sorgenti.zip','archivio/sito-precedente-html.zip','media/achille-tartaruga.mp4']){if(!fs.existsSync(path.join('_build/html',p)))throw new Error(`Risorsa assente: ${p}`);}
console.log(`${list.length} allegati verificati, con archivi e video.`);
