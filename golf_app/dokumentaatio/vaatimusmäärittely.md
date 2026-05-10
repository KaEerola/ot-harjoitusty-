# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi pitää kirjaa pelaamistaan golfkierroksista sekä tarkastella omaa pelikehitystään erilaisten tilastojen avulla. Sovellus mahdollistaa kierrostietojen tallentamisen, selaamisen ja analysoinnin yhdessä paikassa.

## Käyttäjät
Sovelluksen alkuvaiheessa on vain yksi käyttäjätyyppi _normaali käyttäjä_. Sovellukseen lisätään potentiaalisesti tulevaisuudessa esim. _pääkäyttäjä_ jolla on enemmän oikeuksia.

## Käyttöliittymäluonnos
Sovellus koostuu 5 eri näkymästä

![](kuvat/kayttoliittymaluonnos.png)

Sovellus aukeaa kirjautumisnäkymään, josta voidaan siirtyä uuden käyttäjän luomisen näkymään tai kierros listanäkymään.
Kierros listanäkymästä voidaan puolestaan siirtyä joko tilastonäkymään tai kierroksen luomisen näkymään

## Perusversion tarjoama toiminnallisuus
### Ennen kirjautumista
* Käyttäjä voi luoda järjestelmään uuden käyttäjätilin
   * Käyttäjätunnus ei saa olla tyhjä ja sen pitää olla uniikki
* Käyttäjä voi kirjautua sisään omalla käyttäjätunnuksellaan.

### Kirjautumisen jälkeen 
* Käyttäjä voi lisätä uuden kierroksen
* Käyttäjä näkee listan omista lisätyistä kierroksista 
* Käyttäjä voi tarkastella kierroksiin liittyviä perustilastoja kuten keskiarvon, parhaan yksittäisen tuloksen, kierrosten lukumäärän, viimeiset x kierrosta ja viimeisten 10 kierroksen keskiarvo vs kaikkien keskiarvo
* Käyttäjä voi poistaa haluamansa kierroksen
* Käyttäjä voi tilastonäkymässä suodattaa kierrokset jotka lasketaan päivämäärän mukaan.

## Jatkokehitysideoita

* Kierrosten muokkaaminen lisäämisen jälkeen
* Lisätilastot (esim. viimeisten kierrosten keskiarvo, väyläosumaprosentti, puttien lukumäärä tms.)
* Tuloskehityksen graafinen esitys, esim kuvaaja tms
* Usean käyttäjän tuki, perusversio vain siis yhden käyttäjän tarkoitukseen
* Reaalitasoituksen automaattinen laskeminen
* Kenttäkohtaiset tilastot
