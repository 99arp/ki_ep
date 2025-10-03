```mermaid
flowchart LR
    A["'>>>input' <br/>oder<br/>py-Datei"]
    B[Compiler] 
    C[pyc-Modul]
    D[Byte-Code]
    H[Output]
    


    subgraph E[Python Virtual-Machine]
        F[Interpreter]
    end
    A --> B
    B --> D
    C -->|"Imports"| D
    D --> F
    F --> H