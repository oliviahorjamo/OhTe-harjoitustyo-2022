# Vaatimusmäärittely

## Sovelluksen yleiskuvaus

Harjoitustyönä toteutetaan Sudoku -sovellus. Sovelluksessa käyttäjät voivat ratkaista sudokuja. Kirjautuneet käyttäjät näkevät tilastoja
ratkaisemistaan sudokuista ja voivat tallentaa keskeneräisiä ratkaisuja.

## Käyttöliittymä

Sovellukseen täytyy ensin joko kirjautua sisään tai luoda uusi käyttäjä. Tämän jälkeen pääsee etusivulle, missä on lista järjestelmästä löytyvistä sudokuista. Sudokua klikkaamalla saa auki pelinäkymän, missä käyttäjä voi liikkua nuolinäppäimillä ja kirjoittaa ruutuun haluamansa numeron ja poistaa lisäämiään numeroita. Keskeneräinen ratkaisu tallennetaan jokaisen muutoksen jälkeen repositorioon. Sudokun alapuolella on tarjolla _Hae aiempi ratkaisusi_ -painike, mistä käyttäjä voi hakea keskeneräisen ratkaisunsa. Ruudun yläreunassa on koko ajan tarjolla _Kirjaudu ulos_ -painike, josta käyttäjä voi kirjata itsensä ulos.

## Toiminnallisuudet

- Käyttäjä voi luoda järjestelmään uniikin käyttäjätunnuksen, jonka on oltava vähintään 1 merkin pituinen. **Tehty**
- Käyttäjä voi kirjautua sisään. **Tehty**
- Käyttäjä voi pelata järjestelmässä olevia sudokuita. Käyttäjä voi liikkua ruudukossa nuolinäppäimillä, lisätä numeron ruutuun painamalla haluamaansa numeropainiketta. Käyttäjä voi poistaa lisäämänsä numeron painamalle Delete -painiketta. **Tehty** 
- Käyttäjän keskeneräisen sudoku tallennetaan automaattisesti. **Tehty**
- Käyttäjän keskeneräinen ratkaisu haetaan automaattisesti käyttäjän avatessa sudokun. **Tehty**
- Käyttäjä voi kirjautua ulos. **Tehty**

## Jatkokehitysideoita

- Käyttäjä voi tarkastaa tähän mennessä luomansa ratkaisun oikeellisuuden, jolloin järjestelmä herjaa, jos käyttäjä on lisännyt sudokun sääntöjen vastaisesti numeroita. Järjestelmä ei herjaa väärässä paikassa olevia numeroita, jotka eivät ole sääntöjen vastaisia.
- Käyttäjä voi antaa ratkaisemalleen sudokulle arvion vaikeudesta ja kirjallisen arvostelun. Arviot ovat näkyvillä muille käyttäjille.
- Käyttäjä voi poistaa tunnuksensa, jolloin kaikki hänen keskeneräiset ratkaisunsa poistetaan. Arvostelujen kohdalle merkitään tieto, että käyttäjätunnus on poistettu.
