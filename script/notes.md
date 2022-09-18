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



### Slide 2 - Specifika prostredi FEG

#### Reveal

par bodu mozna nejaka infografika k tomu v cem je FEG specificky 

#### Idea

Vypichout hlavne:

- silny inhouse vyvoj
- rozsahle openshift prostredi
- duraz na microsluzby (nedavat do prezentace spis zminit pouze openshift - je to duplicita)
- aplikace ruznych typu (retail, 3rd party, reporting, backoffice)

#### Script

Pojdme se spolu podivat i na specifika prostredi fortuny. V prve rade bych rad zduraznil velke mnozstvi internich a ruznorodych aplikaci ktere jsou vzajemne provazane. Ty se tykaji at uz retail businessu tzn sazeni jako takoveho, ktery je asi nejviditelnejsi casti tak ale i aplikaci pro bookmakery, fraud apod, pripadne pro vymenu data s ruznymi 3rd party sluzbami nebo reportingem do cnb a pod. V takovem prostredi pak vcelku prirozene mame na ruzne sluzby ruzne pozadavky. Chceme aby nektere sluzby byly pristupne bez jakychkoliv omezeni, u nekterych by zase mela byt vyzadovana nejaka forma autentizace, sluzby maji ruznou citlivost, nektere nejsou kriticke u jinych je jejich vypadek velkou neprijemnosti   


#### Todo

- lepe formulovat povidani


---


### Slide 3 - Co je apigw

#### Reveal

podobny diagram jako byl pro cntf apigw. Jen mozna mene objektu

#### Idea

Kratke shrnuti co apigw je a jak ji chapem. Povidani by mohlo obsahovat i informace ktere jsem mel z tabulky ala reverse proxy vs apigw

#### Script

Co apigw vlastne je. Jedna se o reverzni proxy ktera je zamerena na komunikaci s beckendovymi sluzbami a ktere publikuji sva data pres vetsinou pres REST. Slovo data je zde dulezite. Proti standartni proxy jsou zde ale nektere odlisnoti. Zatimco je zemerena vice na infrastrukturu jako takovou kde resime napriklad ssl terminaci apigw se zameruje prave na praci s endpointy a poskytovanymi daty, pristupu k nim jejich transormace apod. REST poskytuje data v tomto ohledu bychom k nim meli take pristupovat. Meli bychom vedet jaka data pulikujeme, komu je publikujeme a kam.

#### Todo

---



### Slide 4 - Pozadavky

#### Reveal
Jednotlive body shrnuji pozadavky na nasi apigw

#### Idea

znovu predstavit projekt, mozna popovidat i jake dalsi varianty jsme zvazovali, 
- pozadavky na apigwp
- mozna subframe kde bude zminen vitez nginx plus
- popsat konsolidaci microservics

#### Script

- TBD

#### Todo

- vsechno

---




### Slide 5 - Geneze projektu

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
- Zduraznit ze se jedna o replikaci
- Pro replikaci potrebujeme cluster inside ocp
- Zminit i nevyhody tohoto reseni - je statefull v k8s svete => dopady na skalovani
- vysvetlit vyhody konfigurace overovani - jednoduchost, ukazka z konfigurace
- odkaz na github na referencni projekt

#### Script

- TBD

#### Todo

---



### Slide 8 - Service discovery v ramci ocp/k8s

#### Reveal

- Priklad konfigurace upstreamu, mozna diagram, mozna screenshot z dashboards

#### Idea

- Vysvetlit vyhody takoveho reseni
- headless svc, srv dns pod discoveryt
- Zmint ze bez teto fce neni mozne delat pokrocile fce jako rate limitng a nebo circuit breaking, a vubec vsechny veci ktere vyzaduji stickyness
- vysvetlit vyhody konfigurace overovani - jednoduchost, ukazka z konfigurace
- odkaz na github na referencni projekt

#### Script

- TBD

#### Todo

---



### Slide 9 - Architektura

#### Reveal

- diagram ukazajici 3 apigw - cloudflare, apigw, svc

#### Idea

- 3 typy apigw
    - interni
    - externi (pro externi partnery)
    - public
- vysvetlit rozdily

#### Script

- TBD

#### Todo

---



### Slide 9 - Deployment v ramci FEGu

#### Reveal

- jednoduchy diagram pozadavek -> swag2nginx -> include file -> template -> helm deploy, mozna ukazka value filu

#### Idea

- Ukazat nas toolset a cely process deploye apigw
- Zminit helm jako klicovou komponenty tohoto procesy
- Jemne zminit architekturu celeho reseni templatu. Tzn jeden master file, includu file per svc, 
    - cfg muze byt
        - include file per svc, ktery popisuje dany endpoint
        - include file pro danny endpoint - napriklad zapnuti cors a nebo jwt autentizace
        - backend modul v lue nebo js
- jeden value file vladne vsem!
- zduraznit ze timto resenim jsme schopni skladat konfiguraci po fcnich blocich
    - pouzit prirovnani jako LEGO

#### Script

- TBD

#### Todo


---



### Slide 10 - NA co nezbyl cas :)

#### Reveal

- par bodu na toto tema

#### Idea

- monitoring and alerting
- error handling
- cors
- logging a integrace s efk stackem
- debugging a tracing


#### Script

- TBD

#### Todo

