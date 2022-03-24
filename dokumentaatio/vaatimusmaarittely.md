# Vaatimusmäärittely

## Sovelluksen yleiskuvaus

Harjoitustyönä toteutetaan Sudoku -sovellus. Sovelluksessa käyttäjät voivat ratkaista sudokuja. Kirjautuneet käyttäjät näkevät tilastoja
ratkaisemistaan sudokuista ja voivat tallentaa keskeneräisiä ratkaisuja.

## Käyttöliittymä

Sovelluksen etusivulla on tarjolla lista sudokuista vaikeustason mukaan luokiteltuna. Etusivulle pääseminen ei vaadi kirjautumista.
Sudokua klikkaamalla saa auki pelinäkymän, missä käyttäjä voi vapaata ruutua klikkaamalla kirjoittaa ruutuun haluamansa numeron.
Käyttöliittymän yläreunassa on koko ajan tarjolla mahdollisuus luoda uusi käyttäjä tai kirjautua sisään. Lisäksi sudokun alapuolella on tarjolla
_Tallenna_ -painike, mitä voi klikata vain kirjautuneena käyttäjänä.

## Toiminnallisuudet

- Käyttäjä voi luoda järjestelmään uniikin käyttäjätunnuksen, jonka on oltava vähintään 3 merkkiä pitkä.
- Käyttäjä voi pelata järjestelmässä olevia sudokuita. Tällöin käyttäjä voi lisätä ja poistaa numeroita ruudukosta. Lisäksi hän voi tarkastaa
tähän mennessä luomansa ratkaisun oikeellisuuden, jolloin järjestelmä herjaa, jos käyttäjä on lisännyt sudokun sääntöjen vastaisesti numeroita.
Järjestelmä ei herjaa väärässä paikassa olevia numeroita, jotka eivät ole sääntöjen vastaisia.
- Kirjautunut käyttäjä voi tallentaa keskeneräisen ratkaisunsa.
- Käyttäjä voi kirjautua ulos.
