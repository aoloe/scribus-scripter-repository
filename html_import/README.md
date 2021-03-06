HTML import feature
===========================
Import html into scribus 

- clean html with tidy
- add or match styles
- use of paragraph styles and caracter styles may be with HTML class detection
- add text to scribus file
- eventually import images

Don't do :
- CSS import

## Analyse d'un exemple en provenance de FmFr

### Hypothèse : 1 fichier HTML pour tout le document

Possibilités d'extension :

- Autre scripts qui ferait des appels successifs pour les imports
- Script qui génère un fichier HTML en sortie à partir du lot

### Etapes:

 - Construire l'arbre XML (libXML)
 - Répertorier toutes les attributs "class", pas les "id" car style unique
   (sauf si même "id" dans des fichiers distincts, ex: pages Wikipedia  
    => à concaténer multiples pages qui transformeraient "id" en "class"  
    => outil à part)
 - Identifier les 2 styles Scribus "paragraphe" et "caractères":
   - Le nom de la classe sera le nom du style
   - Associer le style Scribus "paragraphe" ou "caractère" selon la nature
     de son utilisation dans l'HTML (balises "blocs" ou "en ligne")
     - blocs: h*, p, pre, ul, li, ol, div, ...
     - en ligne: b, i, u, span, strong, emph, ...
     => [Code] Créer 2 listes de balises à traiter
 - Identifier les éléments suivants:
   - images `<img src= alt=>` (tirer la légende de "alt")
   - liens `<a href=>`
   - tables (non gérées: afficher le contenu brut)
 - Traduire les caractères spéciaux (au moins `"&nbsp;"`)

A voir ultérieurement:

 - sélection d'une zone particulière (ex: `<div>` Wikipedia)
 - inclusion des images "inline" ou via ancre (approche préférée)

## Quelques exemples de définition des styles

Pour:

    <p>
    <p class="indente">
    <ul class="indente">

Produire les styles suivants:

 - `Style_p`
 - `Style_p_indente` + parent `Style_p`
 - `Style_ul_indente` (+ parent `Style_ul`)

Exemple de définition CSS:

    # p
    police="arial"

    # indente
    color="red"

    # p indente
    police="deja vu"

    # ul indente


Pour:

 - `<span class="mots-clés">`
 - `<strong class="mots-clés">`

Produire:

 - Style_mots-cles
 - Style_mots-cles

## Besoins pour l'API

- Ecrire du texte dans un cadre texte (transformation au préalable, eg.`&nbsp;` `&.+;`)
  - Méthode "insert()" ou "append()" => "append()" : peut prendre en argument un bout de texte ou le texte complet.
  - existe en tant que :  TextAPI.insertText(text, position)
- Créer un style "paragraphe" ou "caractère" en attribuant un nom et un parent
  -  DocumentAPI.newStyle(StyleName, ParentStyle=None)
  -  (code scribus scribusdoc.cpp) ParagraphStyle.setParent()
  -  DocumentAPI.setStyle(StyleName,propertyName,PropertyValue) : exemple de propertyName : parentStyle, color, font
- Lister les styles existants
  - DocumentAPI.styles.cars()
  - DocumentAPI.styles.para()
- Appliquer le style à une sélection de texte
  - existe : TextAPI.selectText(start, selectCount) 
  - selection.applyStyle(styleName) (scribusdoc.cpp) itemSelection_applyCharStyle
- (Option pour étendre la fonctionnalité à plusieurs pages) Ajouter une page, un cadre (texte/image)

Mis de côté:

 - (pas d'import image pour l'instant) Importer une image dans un cadre image
 - (Besoin géré dans une fonctionnalité à part -- autre sript) : Lier des cadres
