# Vaatimusmäärittely

## Sovelluksen yleiskuvaus

Harjoitustyönä toteutetaan Sudoku -sovellus. Sovelluksessa kirjautuneet käyttäjät voivat ratkaista sudokuja. Käyttäjien keskeneräiset ratkaisut tallennetaan automaattisesti.

## Käyttöliittymä

Sovellukseen täytyy ensin joko kirjautua sisään tai luoda uusi käyttäjä. Tämän jälkeen pääsee etusivulle, missä on lista järjestelmästä löytyvistä sudokuista. Sudokua klikkaamalla saa auki pelinäkymän. Pelinäkymässä näkyy automaattisesti käyttäjän aiemmin luoma keskeneräinen ratkaisu, jos sellainne on olemassa. Käyttäjä voi liikkua pelinäkymässä nuolinäppäimillä ja kirjoittaa ruutuun haluamansa numeron ja poistaa lisäämiään numeroita. Keskeneräinen ratkaisu tallennetaan jokaisen muutoksen jälkeen repositorioon. Pelinäkymästä voi palata takaisin etusivulle Return -painikkeella. Lisäksi ruudun yläreunassa on koko ajan tarjolla _Kirjaudu ulos_ -painike, josta käyttäjä voi kirjata itsensä ulos.

## Toiminnallisuudet

- Käyttäjä voi luoda järjestelmään uniikin käyttäjätunnuksen, jonka on oltava 1-19 merkkiä pitkä. Myös käyttäjätunnukseen liitetyn salasanan on oltava 1-19 merkkiä pitkä.
- Käyttäjä voi kirjautua sisään.
- Käyttäjä voi pelata järjestelmässä olevia sudokuita. Käyttäjä voi liikkua ruudukossa nuolinäppäimillä, lisätä numeron ruutuun painamalla haluamaansa numeropainiketta. Käyttäjä voi poistaa lisäämänsä numeron painamalle Delete -painiketta.
- Käyttäjän keskeneräisen sudoku tallennetaan automaattisesti.
- Käyttäjän keskeneräinen ratkaisu haetaan automaattisesti käyttäjän avatessa sudokun.
- Käyttäjä voi palata pelinäkymästä takaisin etusivulle.
- Käyttäjä voi kirjautua ulos.

## Jatkokehitysideoita

- Käyttäjä voi tarkastaa tähän mennessä luomansa ratkaisun oikeellisuuden, jolloin järjestelmä herjaa, jos käyttäjä on lisännyt sudokun sääntöjen vastaisesti numeroita. Järjestelmä ei herjaa väärässä paikassa olevia numeroita, jotka eivät ole sääntöjen vastaisia.
- Käyttäjä voi antaa ratkaisemalleen sudokulle arvion vaikeudesta ja kirjallisen arvostelun. Arviot ovat näkyvillä muille käyttäjille.
- Käyttäjä voi poistaa tunnuksensa, jolloin kaikki hänen keskeneräiset ratkaisunsa poistetaan. Arvostelujen kohdalle merkitään tieto, että käyttäjätunnus on poistettu.
