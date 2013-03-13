# Script Master Document

Synchroniser le formatage par rapport à un document maître et produire un résultat commun.

## Features

- Gérer une liste de fichier qui dépendent d'un document maître
- Synchroniser les styles par rapport au document maître
- Synchroniser les numéros de page entre les documents
- Synchroniser les gabartits par rapport au document maître
- Exporter les fichiers vers le format de sortie

## Todo

- Ask for the configuration file (yaml) to be read.
- Read the list of styles in the master document.
- Open the first document in the list.
- Make sure that each style exists.
- Overwrite the definition from the styles defined in the master document.

## Manage the list of the project files

La liste des fichiers est gérée dans un fichier de configuration Yaml.

    masterpage: fmfr-template.sla
    files:
    - fmfrsection01.sla
    - fmfrsection02.sla

## Notes

Filter Book
- XML généré
- yaml

## Sync Styles 
(coper style du master document, écraser styles du document courant et redéfinir avec ce qu'on a copié)

## Sync page / footnotes
(aller dans l'ordre des fichiers, prenre le dernier nombre et l'appliquer à l'actuel). Savoir qd un numéro comence de 0.

## Sync master pages
(écraser les master pages qui ont le même nom avec les gabarit qui viennent du master doc)

## Export all to pdf ebook/html
(exporter le tout vers plusieurs pdf, un pdf par fichier et export ebook et html et txt)


