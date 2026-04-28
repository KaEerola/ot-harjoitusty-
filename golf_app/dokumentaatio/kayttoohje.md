# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/kaeerola/ot-harjoitusty-/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

---

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä asenna riippuvuudet komennolla:

```bash
poetry install
```

Tämän jälkeen suorita projektin alustustoimenpiteet:

```bash
poetry run invoke build
```

Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

---

## Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään.

Kirjautuminen tapahtuu syöttämällä olemassa oleva käyttäjänimi ja salasana ja painamalla painiketta **Login**.

Onnistuneen kirjautumisen jälkeen käyttäjä siirtyy päävalikkoon.

---

## Uuden käyttäjän luominen

Kirjautumisnäkymästä voi siirtyä uuden käyttäjän luontiin painamalla painiketta **Create user**.

Uusi käyttäjä luodaan täyttämällä vaaditut kentät ja painamalla **Create**-painiketta.

Onnistuneen luomisen jälkeen käyttäjä kirjataan automaattisesti sisään.

---

## Kierrosten lisääminen

Kirjautumisen jälkeen käyttäjä voi lisätä uuden golfkierroksen.

Kierros lisätään syöttämällä:

* kentän nimi
* tulos
* päivämäärä

ja painamalla painiketta **Add round**.

Lisätty kierros tallentuu käyttäjän omiin tietoihin.

---

## Kierrosten tarkastelu (round_list_view)

Käyttäjän kaikki kierrokset näkyvät näkymässä **round_list_view**.

Näkymä sisältää listan kierroksista, joista näkyy esimerkiksi:

* kentän nimi
* tulos
* päivämäärä

---

## Kierroksen poistaminen

Kierros poistetaan valitsemalla haluttu kierros näkymästä **round_list_view**.

Valinnan jälkeen kierros poistuu järjestelmästä.

---

## Tilastot

Tilastosivulle pääsee painamalla painiketta **Statistics**.

Tilastosivulla näytetään yhteenveto pelatuista kierroksista, kuten:

* keskimääräinen tulos
* paras kierros
* kierrosten kokonaismäärä

---

## Takaisin navigointi

Tilastosivulta ja muista näkymistä voi palata päävalikkoon painamalla painiketta **Back**.

---

## Uloskirjautuminen

Käyttäjä voi kirjautua ulos sovelluksesta painamalla painiketta **Logout**.

Uloskirjautumisen jälkeen käyttäjä palautetaan kirjautumisnäkymään.
