# Ohjelmistotekniikan harjoitustyökurssi

Teen kurssin harjoitustyönä golfsovelluksen, jonka avulla pystyy tarkastelemaan täytettyä kierroksia, ja katsomaan tarkempia tilastoja

## Dokumentaatio

- [Arkkitehtuurikuvaus](golf_app/dokumentaatio/arkkitehtuuri.md)
- [Changelog](golf_app/dokumentaatio/changelog.md)
- [Tuntikirjanpito](golf_app/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](golf_app/dokumentaatio/vaatimusmäärittely.md)
- [Käyttöohje](golf_app/dokumentaatio/kayttoohje.md)

## Release
https://github.com/KaEerola/ot-harjoitusty-/releases/latest

## Sovelluksen asennusohjeet
1. Asenna riippuvuudet komennolla

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
