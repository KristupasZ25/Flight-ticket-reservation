# Skrydžių Rezervavimo Sistema: Ataskaita

## Įžanga

Tai yra labai paprasta skrydžių rezervavimo sistema. Joje yra leidžiama prisijungti prie vartotojo su slaptažodžiu, pasirinkti iš kokio miesto norite išskristi, kur nuvykti, pasirinkti tinkamą datą arba kelionę į vieną pusę, bei bilieto tipą. Įvykdžius rezervaciją, bilietas nuperkamas ir tada galima atsijungti iš paskyros. Programa taip pat išsaugo rezervacijos duomenis ir juos pateikia kitame faile.

## Pagrindinės Funkcijos

- **Skrydžių paieška**: Vartotojai gali pasirinkti išvykimo ir paskirties miestus bei atlikti skrydžių paiešką pagal pasirinktą datą.
- **Bilietų rezervacija**: Po skrydžio pasirinkimo vartotojas gali atlikti bilietų rezervaciją, pasirinkdami bilietų kiekį ir tipą (ekonominė, verslo, pirmoji klasė).
- **Vartotojų valdymas**: Sistema leidžia vartotojams prisijungti, užregistruoti savo užsakymus ir atlikti atsijungimą.

## Naudotos Technologijos

- **Python 3.x**
- **Tkinter** – vartotojo sąsajos kūrimui
- **unittest** – vienetinių testų kūrimui
- **CSV** – duomenų nuoseklumo užtikrinimui

## Funkciniai Reikalavimai

### OOP Principai:

- **Encapsuliacija**: Klasės, tokios kaip `User`, `Flight`, `Ticket` ir `FlightBookingApp`, kapsuliuoja savo duomenis. Pavyzdžiui, metodai kaip `login()` ir `search_flights()` keičia vidinius duomenis ir valdo vartotojo sąveiką, tačiau nepriklauso nuo tiesioginio vartotojo įvedimo.
  
- **Paveldėjimas**: Klasės `EconomyFlight`, `BusinessFlight` ir `FirstClassFlight` paveldi bendrą funkcionalumą iš `Flight` klasės, bet kiekviena iš jų gali turėti specifinį elgesį, pavyzdžiui, kitas bilieto kainas.
  
- **Polimorfizmas**: Pavyzdžiui, metodas `get_ticket_price()` yra naudojamas tiek `Flight`, tiek `Ticket` klasėse, tačiau kiekviena klasė gali grąžinti skirtingą rezultatą priklausomai nuo tipo. Tai leidžia sukurti įvairias klases, kurios dalinasi bendru metodų pavadinimu, tačiau jų įgyvendinimas priklauso nuo objekto tipo.
  
- **Abstrakcija**: Klasės `Flight` ir `Ticket` suteikia bendrą funkcionalumą, kur metodai kaip `get_ticket_price()` ir `get_ticket_info()` veikia skirtinguose objektuose. Tai leidžia naudoti bendrus metodus, nepriklausomai nuo konkrečios klasės, užtikrinant, kad nereikės tiesiogiai žinoti klasės įgyvendinimo detalių.

### Dizaino Modelis:

- **Factory Design Pattern**: Skrydžių objektai yra kuriami naudojant gamyklos dizaino modelį (Factory Design Pattern). Tai leidžia dinamiškai sukurti skrydžių objektus pagal vartotojo pasirinkimą, užtikrinant sistemos lankstumą ir galimybę lengvai plėsti funkcionalumą, pridedant naujų skrydžių tipų.

### CSV Operacijos:

- Sistema skaito ir rašo duomenis į **CSV** failus, kad užtikrintų duomenų nuoseklumą:
  - **users.csv**: Laiko vartotojų informaciją.
  - **flights.csv**: Laiko skrydžių duomenis.
  - **bookings.csv**: Laiko užsakymų duomenis.

## Testavimas

Norint užtikrinti sistemos patikimumą, buvo sukurtas vienetinių testų rinkinys naudojant Python **unittest** framework'ą. Testuotos funkcijos apima:

- **Skrydžių užsakymas**: Testas patikrina, ar vartotojas gali užsisakyti skrydį ir ar užsakymas yra teisingai išsaugotas.
- **Skrydžių prieinamumas**: Testas tikrina, ar skrydžiai yra teisingai pažymėti kaip užimti per nurodytą laiką.
- **Užsakymo atšaukimas**: Testas tikrina, ar užsakymas gali būti teisingai atšauktas.
- **CSV nuoseklumas**: Testai buvo sukurti tikrinant, ar duomenys teisingai saugomi ir įkeliami iš CSV failų.

## Rezultatai ir Išvados

Sistema sukurta remiantis pagal funkcinius reikalavimus. Gauti rezultatai, tokie, kad programa leidžia:

- Prisijungti prie vartotojo ir nuo jo atsijungti.
- Rezervuoti skrydį pagal duotus kriterijus.
- Užbaigti rezervaciją, pažiūrėti galutinę kainą ir užsakymo informaciją.
- Išsaugoti rezervacijos duomenis naudojant CSV failus.

Kuriant šią sistemą buvo stengiamasi atitikti kuo daugiau reikalavimų, pavyko atlikti didžiąją dalį. 
