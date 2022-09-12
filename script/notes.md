### Slide 1 - Uvod

#### Reveal

Uvodni slajd ala ocp konference

#### Idea

Predstaveni se 

#### Script

Dobry den, vitam Vas na me kratke prednasce kde bych se s Vami rad podelil o zkusenosti s budovanim
apigw na platforme nginx plus v ramci Fortuny. V uvodu mi dovolte abych se predstavil, jmenuji si Honza
Dvorak, v enterprise it se pohybuju uz vice nez 20 let a v soucasne dobe funguji jako hlavne jako kontraktor
pro Fortunu kde mam na starosti prave projekt Apigw a to hlavne po technicke strance

#### Todo

---



### Slide 2 - Co je apigw

#### Reveal

podobny diagram jako byl pro cntf apigw. Jen mozna mene objektu

#### Idea

Kratke shrnuti co apigw je a jak ji chapem. Povidani by mohlo obsahovat i informace ktere jsem mel z tabulky ala reverse proxy vs apigw

#### Script

Na zacatek se pojdme podivat co apigw vlastne je. V podstate se jedna o reverzni proxy ktera je zamerena na komunikaci 
s beckendovymi sluzbami a ktere publikuji sva data pres vetsinou pres REST. Slovo data je zde dulezite. Proti standartni proxy jsou zde ale nektere odlisnoti. Zatimco je zemerena vice na infrastrukturu jako takovou kde resime napriklad ssl terminaci apigw se zameruje prave na praci s endpointy a poskytovanymi daty, pristupu k nim jejich transormace apod. REST poskytuje data v tomto ohledu bychom k nim meli take pristupovat. Meli bychom vedet jaka data pulikujeme, komu je publikujeme a kam.

#### Todo

---



### Slide 3 - Specifika prostredi FEG

#### Reveal

par bodu mozna nejaka infografika k tomu v cem je FEG specificky 

#### Idea

Vypichout hlavne:

- silny inhouse vyvoj
- rozsahle openshift prostredi
- duraz na microsluzby
- aplikace ruznych typu (retail, 3rd party, reporting, backoffice)

#### Script

Pojdme se spolu podivat i na specifika prostredi fortuny. V prve rade bych rad zduraznil velke mnozstvi internich a ruznorodych aplikaci ktere jsou vzajemne provazane. Ty se tykaji at uz retail businessu tzn sazeni jako takoveho, ktery je asi nejviditelnejsi casti tak ale i aplikaci pro bookmakery, fraud apod, pripadne pro vymenu data s ruznymi 3rd party sluzbami nebo reportingem do cnb a pod. Tim vznika i ruzna potreba 


#### Todo

- lepe formulovat povidani

---



### Slide 4 - Geneze projektu

#### Reveal

Timelina kde bude vyznacen, pilot, eveluace, nasazeni prvnich endpointu, live3 s novou autentizaci, dalsi aplikace

#### Idea

znovu predstavit projekt, mozna popovidat i jake dalsi varianty jsme zvazovali, 
- mozna subframe kde bude zminen vitez nginx plus
- popsat konsolidaci microservics

#### Script

- TBD

#### Todo

- vsechno

---



### Slide 6 - Dulezite vlastnosti nginx plus

#### Reveal

par bodu, mozna nejaka infografika

#### Idea

Predstavit jake funkce z placene subscripce vyuzivame

- podpora oidc
- distribuovana keyval db
- service discovery v ramci k8s/ocp
- vestavene openresty a modul njs
- V budoucnu circuit breaking a rate limiting

#### Script

- TBD

#### Todo

- vsechno

---



### Slide 7 - Klicova vlastnost oidc plus keyval db

#### Reveal

diagram v python diagrams kde bude v bodech ukazano jak pracuje state full nginx v k8s. 

#### Idea

- Vysvetlit jak oidc code flow funguje a jak funguje nasledujici overovani.
- Zminit i nevyhody tohoto reseni - je statefull v k8s svete => dopady na skalovani

#### Script

- TBD

#### Todo





