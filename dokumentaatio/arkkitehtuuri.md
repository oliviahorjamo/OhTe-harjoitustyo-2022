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
  participant olivia
  User->>LoginView: click "Create user" button
  LoginView->>SudokuService: create_user("olivia", "olivia123")
  SudokuService->>UserRepository: find_by_username("olivia")
  UserRepository-->>SudokuService: None
  SudokuService->> olivia: User("olivia", "olivia123)
  SudokuService->>UserRepository: create(olivia)
  UserRepository-->>SudokuService: user
  LoginView -->> Mainpage: start()
```

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant TodoService
  participant UserRepository
  participant matti
  User->>UI: click "Create user" button
  UI->>TodoService: create_user("matti", "matti123")
  TodoService->>UserRepository: find_by_username("matti")
  UserRepository-->>TodoService: None
  TodoService->>matti: User("matti", "matti123")
  TodoService->>UserRepository: create(matti)
  UserRepository-->>TodoService: user
  TodoService-->>UI: user
  UI->>UI: show_todos_view()
```
