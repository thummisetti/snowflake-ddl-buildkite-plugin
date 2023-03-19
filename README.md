# Snowflake DDL Buildkite Plugin

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

## Configuration

### Required

### `snowflake_account` (required, string)

The full name of the snowflake account you want to deploy to.

Example: `snowflake-company`

### `snowflake_user` (required, string)

The directory in your repository where are you storing the schemas for your tables and views.

Example: `snowflake_ddl_user`

### `prod_build_branch` (optional, string)

Default branch for the repo.

Example: `main`

Default: `master`

### `fail_pipeline_on_first_exception` (optional, boolean)

Whether to fail pipeline as soon as there is one failure.

Example: `true`

Default: `true`

## License

MIT (see [LICENSE](LICENSE))
