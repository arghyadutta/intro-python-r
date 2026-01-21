# Basic Programming Logic — Mermaid Diagrams

## Sequential Execution

```mermaid
flowchart TD
    A[Start] --> B[Read input]
    B --> C[Process data]
    C --> D[Output result]
    D --> E[End]
```

## Conditional Logic (if / else)

```mermaid
flowchart TD
    A[Start] --> B{Condition true?}
    B -- Yes --> C[Execute block A]
    B -- No --> D[Execute block B]
    C --> E[End]
    D --> E
```

## Multiple Conditions (if / else if / else)

```mermaid
flowchart TD
    A[Start] --> B{Condition 1?}
    B -- Yes --> C[Action 1]
    B -- No --> D{Condition 2?}
    D -- Yes --> E[Action 2]
    D -- No --> F[Default action]
    C --> G[End]
    E --> G
    F --> G
```

## Looping Logic (while loop)

```mermaid
flowchart TD
    A[Start] --> B{Condition true?}
    B -- Yes --> C[Execute loop body]
    C --> B
    B -- No --> D[Exit loop]
    D --> E[End]
```

## Counter-Controlled Loop (for loop)

```mermaid
flowchart TD
    A[Start] --> B[Initialize counter]
    B --> C{Counter < limit?}
    C -- Yes --> D[Execute body]
    D --> E[Increment counter]
    E --> C
    C -- No --> F[End]
```

## Function Call and Return

```mermaid
flowchart TD
    A[Main program] --> B[Call function]
    B --> C[Function body]
    C --> D[Return value]
    D --> A
```

## Nested Control Flow

```mermaid
flowchart TD
    A[Start] --> B{More items?}
    B -- Yes --> C{Item valid?}
    C -- Yes --> D[Process item]
    C -- No --> E[Skip item]
    D --> B
    E --> B
    B -- No --> F[End]
```

## Data Flow

```mermaid
flowchart LR
    A[Input data] --> B[Validate]
    B --> C[Transform]
    C --> D[Store / Display]
```
