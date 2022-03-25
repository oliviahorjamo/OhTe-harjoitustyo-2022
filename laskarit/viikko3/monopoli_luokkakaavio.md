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
      Pelinappula "0...8" -- "*" SattumaJaYhteismaa
      Pelinappula "0..8" -- "*" AsematJaLaitokset
      Pelinappula "0...8" -- "*" NormaalitKadut
      Pelinappula "0...8" -- "1" Vankila
      NormaalitKadut "*" -- "1" Pelaaja
      Talo "1...4" -- "1" NormaalitKadut
      Hotelli "0...1" -- "1" NormaalitKadut
      Raha "*" -- "1" Pelaaja
      Toimintakortti "*" -- "1" SattumaJaYhteismaa
      Toimintakortti "1" -- "1" Toiminto
      SattumaJaYhteismaa "1" -- "1" Toiminto
      AsematJaLaitokset "1" -- "1" Toiminto
      NormaalitKadut "1" -- "1" Toiminto
      Aloitus "1" -- "1" Toiminto
      Vankila "1" -- "1" Toiminto
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
      class NormaalitKadut{
      nimi
      }
      class Toiminto{
      laatu
      }
      
```
