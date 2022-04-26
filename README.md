# OhTe projekti - SudokuGame

Projektina toteutetaan kurssin esimerkkiprojektien listasta Sudoku -sovellus. 

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/oliviahorjamo/OhTe-harjoitustyo-2022/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/oliviahorjamo/OhTe-harjoitustyo-2022/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/oliviahorjamo/OhTe-harjoitustyo-2022/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/oliviahorjamo/OhTe-harjoitustyo-2022/blob/master/dokumentaatio/arkkitehtuuri.md)

## Komentorivitoiminnot

## Tietokannan alustaminen
Ohjelman käyttämän tietokannan voi alustaa komennolla
```bash
poetry run invoke build
```

### Ohjelman suorittaminen
Ohjelman voi suorittaa komennolla

```bash
poetry run invoke start
```

### Testaaminen
Ohjelman testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

Raportti luodaan _htmlcov_-hakemistoon.

### Pylint -raportin luominen

Pylint -raportin voi luoda komennolla:

```bash
poetry run invoke lint
```

### Pylint virheiden korjaaminen

Koodin voi formatoida pylint -ohjeiden mukaiseksi komennolla:

```bash
poetry run invoke format
```
