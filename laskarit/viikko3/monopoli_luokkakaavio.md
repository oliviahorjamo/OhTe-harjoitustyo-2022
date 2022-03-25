Tehtävä 1: Monopoli -pelin luokkakaavio

- 2 noppaa
- pelaajia 2-8
- pelilauta
- pelilaudassa 40 ruutua
- ruutu tietää mikä on seuraava ruutu pelilaudalla
- yksi pelinappula per pelaaja
- pelinappula on aina yhdessä ruudussa

```mermaid
 classDiagram
      Monopoli "1" -- "1" Pelilauta
      Monopoli "1" -- "2...8" Pelaaja
      Monopoli "1" -- "2" Noppa
      Pelaaja "1" -- "1" Pelinappula
      Pelinappula "0...8" -- "1" Ruutu
      Pelilauta "1" -- "40" Ruutu
      
      class Noppa{
      }
      class Pelilauta{
      }
      class Ruutu{
          nimi
      }
      Class Pelinappula{
           nimi
      }
      Class Pelaaja{
           nimi
      }
```
