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
      Pelinappula "0...8" -- "1" Aloitusruutu
      Monopoli "1" -- "1" Aloitusruutu
      Monopoli "1" -- "1" Vankila
      Pelinappula "0...8" -- "*" Sattuma ja yhteismaa
      Pelinappula "0..8" -- "*" "Asemat ja laitokset"
      Pelinappula "0...8" -- "*" Normaalit kadut
      "Normaalit kadut" "*" -- "1" Pelaaja
      Talo "1...4" -- "1" "Normaalit kadut"
      Hotelli "0...1" -- "1" "Normaalit kadut"
      Pelilauta "1" -- "40" Ruutu
      Raha "*" -- "1" Pelaaja
      Toimintakortti "*" -- "1" "Sattuma ja yhteismaa"
      Toimintakortti "1" -- "1" Toiminto
      class Noppa{
      arvo
      }
      class Pelaaja{
      nimi
      }
      class Pelinappula{
      pelaajan nimi
      väri
      }
      class Ruutu{
      nimi
      }
      class Raha{
      arvo
      }
      class "Normaalit kadut"{
      nimi
      }
      class Toiminto{
      laatu
      }
      
```
