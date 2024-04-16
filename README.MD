# Database Indexer

## Description

This is a simple database indexer that reads account combination based files, and indexes them into a database. The database is a simple SQLite database that contains the account combinations and the index of the account combination in the file.

## Requirement

`pip3 install -r requirements.txt`

## Usage

Put your account combination files in the `combolists` directory. The files should be in the following format: `<account>:<password>` per line.

Create a database by running `python3 generate_sql.py`.

Run the server by running `python3 server.py`.

The server will be running <a href="http://127.0.0.1:5000">Here</a> by default.

## API (Kind of sucks :v )

### [GET /index](./request.py)

## License [The Unlicense](./LICENSE) (Public Domain, credits are appreciated)