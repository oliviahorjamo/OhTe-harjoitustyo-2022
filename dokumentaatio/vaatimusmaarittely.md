# Vaatimusmäärittely

## Sovelluksen yleiskuvaus

Harjoitustyönä toteutetaan Sudoku -sovellus. Sovelluksessa käyttäjät voivat ratkaista sudokuja. Kirjautuneet käyttäjät näkevät tilastoja
ratkaisemistaan sudokuista ja voivat tallentaa keskeneräisiä ratkaisuja.

## Käyttöliittymä

Sovellukseen täytyy ensin joko kirjautua sisään tai luoda uusi käyttäjä. Tämän jälkeen pääsee etusivulle, missä on lista järjestelmästä löytyvistä sudokuista. Sudokua klikkaamalla saa auki pelinäkymän, missä käyttäjä voi liikkua nuolinäppäimillä ja kirjoittaa ruutuun haluamansa numeron ja poistaa lisäämiään numeroita. Sudokun alapuolella on tarjolla _Hae aiempi ratkaisusi_ -painike, mistä käyttäjä voi hakea aiemmin tallentamansa keskeneräisen ratkaisun kyseiseen sudokuun. Lisäksi sudokun alapuolella on tarjolla _Tallenna_ -painike, mistä voi tallentaa keskeneräisen ratkaisun. Ruudun yläreunassa on koko ajan tarjolla _Kirjaudu ulos_ -painike, josta käyttäjä voi kirjata itsensä ulos.

## Toiminnallisuudet

- Käyttäjä voi luoda järjestelmään uniikin käyttäjätunnuksen, jonka on oltava vähintään 1 merkin pituinen. **Tehty**
- Käyttäjä voi kirjautua sisään. **Tehty**
- Käyttäjä voi pelata järjestelmässä olevia sudokuita. Käyttäjä voi liikkua ruudukossa nuolinäppäimillä, lisätä numeron ruutuun painamalla haluamaansa numeropainiketta. Käyttäjä voi poistaa lisäämänsä numeron painamalle Delete -painiketta. **Tehty** 
- Kun käyttäjä on pelannut koko sudokun, käyttöliittymä ilmoittaa onko ratkaisu oikea.
- Kirjautunut käyttäjä voi tallentaa keskeneräisen ratkaisunsa.
- Käyttäjä voi kirjautua ulos.

## Jatkokehitysideoita

- Käyttäjä voi tarkastaa tähän mennessä luomansa ratkaisun oikeellisuuden, jolloin järjestelmä herjaa, jos käyttäjä on lisännyt sudokun sääntöjen vastaisesti numeroita. Järjestelmä ei herjaa väärässä paikassa olevia numeroita, jotka eivät ole sääntöjen vastaisia.
- Käyttäjä voi antaa ratkaisemalleen sudokulle arvion vaikeudesta ja kirjallisen arvostelun. Arviot ovat näkyvillä muille käyttäjille.
- Käyttäjä voi poistaa tunnuksensa, jolloin kaikki hänen keskeneräiset ratkaisunsa poistetaan. Arvostelujen kohdalle merkitään tieto, että
- käyttäjätunnus on poistettu.
