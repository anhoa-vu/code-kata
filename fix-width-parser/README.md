# Fixed-Width File Parser

This application parses a fixed-width file based on a specification file and generates a CSV file as output. It is designed to run in a Docker container, making it easy to use and deploy without worrying about environment dependencies.

## Requirements

- Docker installed on your machine.

## Files

- `parser.py`: The main script that performs the parsing.
- `spec.txt`: The specification file that defines the structure of the fixed-width data.
- `data.txt`: The fixed-width data file to be parsed.
- `Dockerfile`: The Dockerfile used to build the Docker image.

## Usage

To run the parser using Docker, you can execute these following commands in your terminal:
  
```bash
docker build -t fixed-width-parser .
```
```bash
docker run --rm fixed-width-parser --help
```
```bash
docker run --rm  -v $(pwd):/app  fixed-width-parser  spec.txt  data.txt  output.csv  --encoding  utf-8
```


### Explanation of the Command
- `docker  run`:  The  command  to  run  a  container.
- `--rm`:  Automatically  remove  the  container  when  it  exits.
- `-v $(pwd):/app`:  Mount  the  current  directory  to  /app  inside  the  container.  This  allows  the  script  to  read  input  files  and  write  the  output  file  in  the  same  directory.
- `fixed-width-parser`:  The  name  of  the  Docker  image.
- `spec.txt,  data.txt,  output.csv`:  Arguments  passed  to  the  script (specification file,  fixed-width  data  file,  and  output  CSV  file).
- `--encoding  utf-8`:  Optional  argument  to  specify  the  encoding  for  reading  and  writing  files.  You  can  change  this  to  ascii  or  other  encodings  as  needed.