import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
def main(count):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello World!")

if __name__ == '__main__':
    # from anyconfig import load
    import anyconfig 
    anyconfig.load
    main()