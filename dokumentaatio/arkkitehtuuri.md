## Luokka-/pakkauskaavio sovelluksesta

Oheinen luokka-/pakkauskaavio kuvastaa sovelluksen luokkien suhdetta toisiinsa.

```mermaid
 classDiagram
      class User{
          username
          password
      }
      class Sudoku{
          grid
      }
      class OriginalSudoku{
          id
          grid
      }
      class SudokuService{
      }
      class ViewSudoku{
          sudoku_id
          cell_size etc.
      }
      class ViewLogin{
      }
      class UserRepository{
      }
      class SudokuRepository{
      }
      ViewSudoku --> SudokuService
      ViewLogin --> SudokuService
      SudokuService --> "0..1" User
      SudokuService --> "0..1" Sudoku
      SudokuService --> UserRepository
      UserRepository --> User
      SudokuService --> SudokuRepository
      SudokuRepository --> Sudoku
      Sudoku --> OriginalSudoku
      OriginalSudokuRepository --> OriginalSudoku
      SudokuService --> OriginalSudokuRepository
```

## Sekvenssikaavio uuden käyttäjän luomisesta

Kun uusi käyttäjä kirjautuu sovellukseen, kontrolli etenee seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant LoginView
  participant SudokuService
  participant UserRepository
  participant Mainpage
  participant masa
  User->>LoginView: click "Create user" button
  LoginView->>SudokuService: create_user("masa", "masa123")
  SudokuService->>UserRepository: find_by_username("masa")
  UserRepository-->>SudokuService: None
  SudokuService->>masa: User("masa", "masa123")
  SudokuService->>UserRepository: create(masa)
  UserRepository-->>SudokuService: user
  LoginView -->> Mainpage: start()
```
