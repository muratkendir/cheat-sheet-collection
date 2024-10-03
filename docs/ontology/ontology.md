# Ontology RDF/OWL Notes

## Terminology

**Asserted Hierarchy** : {TR} Bildirilen Hiyerarşi

**Inferred Hierarchy** : {TR} Çıkarsanmış Hiyerarşi
(Hierarchies created by "Reasoners")

**Necessary Condition** (Primitive Class)

SubClassOf : Cheesy Pizza hasTopping CheeseTopping.

{TR} "Peynirli Pizza" sınıfındaki tüm pizzalarda peynir malzemesi olması gerekir. Bu ortaya konabiliyorsa, önceki önerme "Gereklilik Koşulu"dur. (Necessary Condition)  

**Necessary & Sufficient Condition** (Defined Class)

SubClassOf (Anonymous Ancestor) : Cheesy Pizza has Topping CheeseTopping.

{TR} 
- "Peynirli Pizza" sınıfındaki tüm pizzalarda peynir malzemesi olması gerekir.
- "PeynirMalzemesi" gereklilik koşulunu sağlayan tüm pizzalar, peynrili pizzadır.

Bu iki önerme ortaya konabiliyorsa, önceki önerme, gerekli ve yeterli olma koşulu'dur. (Necessary & Sufficient Condition)

**Universal Restriction** / ∀ / "All Values From" / "only"

*All* VegeterianPizza hasTopping *only* (CheeseTopping *or* VegetableTopping).

{TR} *Bütün* VejeteryanPizza(larda), vardır, sadece (PeynirMalzemesi veya SebzeMalzemesi).

- Gerekli ve yeterli koşul olduğu için "Tanımlanmış Sınıf"a (Defined Class) dönüştürülebilir.

**OWA/Open World Assumption** : Bir sınıfın tanımının yapılmamış olması, o sınıfın var olmadığı anlamına gelmez.

**Closure Axiom** : {TR} Kapatan Önerme

{TR} 
1) İçinde *sadece* (peynir veya sebze malzemesi) olan *tüm* pizzalar, vejeteryan pizzadır. 
2) Margerita Pizza, şu içeriğe sahiptir; *bazı* peynir malzemesi

1+2) Önermelerini dikkate alınarak çalışacak olan "Reasoner"lar, Margerita Pizza'yı vejeteryan pizza olarak tanımlamayacaklar. Nedeni, Margerita Pizza'da *bazı* peynir malzemesi olduğunu biliyoruz, ancak et ürünü olup olmadığını bilmiyoruz. 

Alternatif 2) Margerita Pizza, şu içeriğe sahiptir; *sadece* peynir malzemesi.

1+Alternatif 2) Bu durumda, Margerita Pizza, VejeteryanPizza olarak Reasoner'lar tarafından tanımlanabilir.

**Range (Intersection)** : {TR} Hedef Alan

Pizza hasBase *PizzaBase*.

{TR} Hedef Alan, pizza tabanıdır. (Pizza Base)

Eğer bu alanda birden fazla sınıf varsa, bu sınıfların kesişimine hedef alan denir.

VegetarianPizza hasTopping only (CheeseTopping or VegetableTopping).

**Domain** : Öznel Alan

*Pizza* hasBase PizzaBase.

Note: Domain and Range do not act as constraint.
{TR} Not: Öznel Alan ve Hedef Alan , kısıtlama olarak davranmaz. 

**Property Restriction** : {TR} Özellik/İlişki Kısıtlamaları

1) Quantifier : {TR} Nicelik
    1-a) Existential (∃) / "SomeValuesFrom"  : {TR} Kısmi
    1-b) Universal (∀) / "AllValuesFrom" : {TR} Bütünsel
2) Cardinality : {TR} Önemlilik
3) hasValue : {TR} Öznitelik

MargeritaPizza hasTopping **some (∃)** TomatoTopping.
MargeritaPizza hasTopping **some (∃)** MozarellaTopping.

{TR} En az 1 Mozarella ve en az 1 domates malzemesi olan pizza Margerita Pizzadır. Buradaki kısıtlama (1a) kısmi-nicelikseldir. (quantifier-existential)

## Relation Types

### DISJOINT: {TR} Ayrık Eleman

Pizza  is **disjoint** with PizzaTopping and PizzaBase.
{TR}
Pizza tabanı, pizza olamaz.
Pizza malzemesi, pizza olamaz.

### SIBLING: {TR} Kardeş (eş düzeyde / eküri) eleman

SeepPanBase and ThinCrispyBase are **sibling**s.
{TR}
Kalın hamur ve ince hamur eş düzeyde elemanlardır.
Kalın hamur ve ince hamur, pizza tabanının alt-sınıfıdır. (SubClassOf)

### OBJECT PROPERTY: {TR} İlişki

Pizza **hasIngredient** Base.
{TR}
Pizza şu içeriğe sahiptir: Pizza Tabanı.

### INVERSE PROPERTY: {TR} Tersinir İlişki (Tersi de geçerli olan)
Base isIngredientOf Pizza.
Pizza hasIngredient Base.

### FUNCTIONAL PROPERTY (Single Valued Properties): {TR} Tek nesne ile kurulabilen ilişki
{TR}
Osman şuAnneyeSahiptir: Ayşe.
Osman şuAnneyeSahiptir: Fatma.
"şuAnnayeSahiptir" ilişkisi fonksiyonel ise Ayşe ve Fatma aynı kişidir.

### INVERSE FUNCTIONAL PROPERTY: {TR}

Ayşe, şuKişininAnnesidir: Osman.
Fatma, şuKişininAnnesidir: Osman.
"şuKişininAnnesidir" ilişkisi, "şuAnnyeSahiptir" ilişkisinin ters fonksiyonu ise, yine Ayşe ve Fatma'nın aynı kişi olduğu söylenir.

### TRANSITIVE PROPERTY : {TR} Kalıtımsal İlişki

Mathew **hasAncestor** *Peter*.
*Peter* **hasAncestor** William.

If "hasAncestor" transitive property, then it can be said that "Mathew hasAncestor William."

<blockquote>
If property is transitive, then inverse property should alsobe transitive.
For exp: 
1) Peter isDescendantOf Mathew.
2) William isDescendantOf Peter.
1+2) William isDescendantOf Mathew.
{TR} Eğer ilişki kalıtımsal ise, ters ilişki de kalıtımsaldır.
</blockquote>

<blockquote>
If property is transitive, then it can not be functional.
{TR} Eğer ilişki kalıtımsal ise, fonksiyonel olamaz.
</blockquote>

### SYMMETRIC PROPERTY: {TR} Simetrik İlişki

Mathew **hasSibling** Gemma.
If "hasSibling" symmetric property, then it can be said that "Gemma hasSibling Mathew."

### ASYMMETRIC PROPERTY: {TR} Asimetrik İlişki
{TR}
Robert şuKişininÇocuğudur: David.
"şuKişininÇocuğudur" asimetrik ilişki ise, "David şuKişininÇocuğudur: Robert." yanlış önerme olur.

### REFLEXIVE PROPERTY: {TR} Refleksif (Yansıyan) İlişki
George knows Simone.
If "knows" property is reflexive, then it can be said that:
- George knows George.
- Simone knows Simone.

### IRREFLEXIVE PROPERTY: {TR} Refleksif olmayan (Yansımayan) ilişki
Alice isMotherOf Bob.
If "isMotherOf" property is irreflexive, then it can be said that:
- Alice isNOTMotherOf Alice.
- Bob isNOTMotherOf Bob.








 
