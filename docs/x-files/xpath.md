# XPath

## Kind of Nodes

Element, Attribute, Text, Namespace, Processing/Instruction, Comment, Root

## Expressions and Wildcards

**Expression** | **Description** | **Açıklama(TR)** | **Examples**
--- | --- | --- | ---
nodename | Selects all nodes with the name "nodename" | "nodename" ismine sahip bütün düğümler | ---
/ | Selects from the root node | Kök düğüm | ---
// | Selects nodes in the document from the current node that match the selection no matter where they are | Mevcut düğümden itibaren, nerede olduğuna bakmaksızın eşleşen ilk düğüm | ---
. | Selects the cuırrent node | Mevcut düğüm | ---
.. | Selects the parent of the current node | Baba düğüm | ---
@ | Selects Attributes | Öznitelik | ---
* | Matches any element node | Eşleşen herhangi bir düğüm | ---
@* | Matches any element node | Eşeleşen herhangi bir öznitelik | ---
node() | Matches any node of any kind | Herhangi bir türdeki herhangi bir düğüm | name(), local-name(), namepsace-uri(), position()
--- | --- | --- | ---
<br>
**Example** | **Description** | **Açıklama(TR)**
--- | --- | ---
/bookstore/* | --- | "bookstore" içindeki herhangi bir düğüm
//* | --- | Mevcuttan itibaren dökümandaki herhangi bir düğüm
//title[@*] | --- | Özniteliği olan herhangi bir "title" türündeki düğüm
--- | --- | ---
<br>

## Predicates and Operators

**PREDICATE/Belirteç** | **Description** | **Açıklama(TR)**
--- | --- | ---
book[1] | Frist node in book | "Book" elemanı içindeki ilk (çocuk) düğüm
book[last()] | Last node in book | "Book" içindeki son (çocuk) düğüm
[last()-1] | Last but one | Sondan bir önceki
[position<3] | First two nodes | İlk iki düğüm
//title[@lang] | Any "title" nodes with a "lang" attribute | Düğüm adı "title" olup, "lang" isimli bir özniteliği olan düğümler
/bookstore/book[price>35.00] | Alt books in bookstore which are expensive than 35 unit | "Bookstore" içindeki "Book"larda fiyatı 35'den fazla olanlar
--- | --- | ---
<br>
**OPERATOR** | **Description** | **Açıklama(TR)**
--- | --- | ---
//book/title ```||``` //book/price | Double pipe used as AND | "Book" içindeki "title"lar VE "book" içindeki "price"lar
//book ```|``` //cd | --- | İki düğümü bir araya getirir.
(+), (-), (div), (*), (=) | --- | Aritmetik operatörler
--- | --- | ---
<br>

## Axes

**AXE/Eksen** | **Description** | **Açıklama(TR)**
--- | --- | ---
Ancestor | Selects all ancestors (parent, grandparent, etc.) of the current node | Bir düğümün bütün ATAları
ancestor-or-self | Selects all ancestors (parent, grandparent, etc.) of the current node and the current node itself | Bir düğümün ATAları ve kendisi
attribute | Selects all attributes of the current node | Bir düğümün bütün ÖZNİTELİKleri
child | Selects all children of the current node | Bir düğümün bütün ÇOCUKları
descendant | Selects all descendants (children, grandchildren, etc.) of the current node | Bir düğümün bütün (alt)NESİLleri
decendant-or-self | Selects all descendants (children, grandchildren, etc.) of the current node and the current node itself | Bir düğümün bütün (alt)NESİLleri ve kendisi
following | Selects everything in the document after the closing tag of the current node | Dökümanda mevcut düğümden SONRAKİ her şey
following-sibling | Selects all siblings after the current node | Mevcut düğümden sonraki bütün KARDEŞ düğümler
namespace | Selects all namespace nodes of the current node | Mevcut düğümün bütün AD ALANI(namespace) düğümleri
parent | Selects the parent of the current node | Mevcut düğümün EBEVEYNi
preceding | Selects all nodes that appear before the current node in the document, except ancestors, attribute nodes and namespace nodes | Mevcut düğümden önceki (Mevcudun ATAsı, Özniteliği, Ad Alanı (namespace) hariç) bütün düğümler
preceding-sibling | Selects all siblings before the current node | Mevcut düğümden önceki bütün akrdeş düğümler
self | Selects the current node | Mevcut düğümün KENDİsi
--- | --- | ---
<br>

## Examples

**Example** | **Description** | **Açıklama(TR)**
--- | --- | ---
child::book | Selects all book nodes that are children of the current node | "Book" elemanının bütün ÇOCUKları
attribute::lang | Selects the lang attribute of the current node | "lang" ÖZNİTELİĞİ
child::* | Selects all element children of the current node | bütün ÇOCUKları
attribute::* | Selects all attributes of the current node | Bütün ÖZNİTELİKleri
child::text() | Selects all text node children of the current node | Çocuk düğümlerdeki bütün metin (Text) düğümleri
child::node() | Selects all children of the current node | Bütün ÇOCUK düğümler
descendant::book | Selects all book descendants of the current node | "Book"un bütün (alt)NESİL düğümleri
ancestor::book | Selects all book ancestors of the current node | "Book"un bütün ATA düğümleri
ancestor-or-self::book | Selects all book ancestors of the current node - and the current as well if it is a book node | "Book"un bütün ATAları ve KENDİsi
child::*/child::price | Selects all price grandchildren of the current node | Mevcut düğümün bütün çocuklarının çocuklarının (torunların) "price" düğümleri
--- | --- | ---
