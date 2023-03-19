# Library Example Buildkite Plugin [![Build status](https://badge.buildkite.com/acf3e41311e5819510cb28c2834de9fe39b2d9931b69d87f4a.svg?branch=master)](https://buildkite.com/buildkite/plugins-library-example)

A buildkite plugin to deploy DDL to your snowflake database by directly running SQL files from the repo, using the snowflake-python connector.

It works by providing [an `environment` hook](hooks/environment) which updates `$PATH` to include the `bin` directory containing the additional commands to expose to build jobs.


## Usage

```yml
steps:
  # Run the included new-ddl-deploy script that runs a Docker container
  - command: new-ddl-deploy
    plugins:
      - snowflake-ddl-buildkite-plugin#v1.0.1: ~
```

## License

MIT (see [LICENSE](LICENSE))
