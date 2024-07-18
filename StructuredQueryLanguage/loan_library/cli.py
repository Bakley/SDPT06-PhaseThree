import click
from datetime import date
from services.author_service import AuthorService

author_service = AuthorService()

@click.group()
def cli():
    """Library Management System"""
    pass

@click.command()
@click.argument('name')
def add_author(name):
    """Add a new author record"""
    author_service.add_author(name)
    click.echo(f'Author "{name} added"')
@click.command()
@click.argument('name')
def add_author(name):
    click.echo(f'Author "{name}" added.')

@click.command()
def list_authors():
    click.echo('Listing all authors.')
    authors = author_service.list_authors()
    for author in authors:
        click.echo(f'ID: {author[0]}, Name: {author[1]}')

@click.command()
@click.argument('author_id', type=int)
@click.argument('name')
def update_author(author_id, name):
    click.echo(f'Author with ID {author_id} updated to "{name}".')

@click.command()
@click.argument('author_id', type=int)
def delete_author(author_id):
    click.echo(f'Author with ID {author_id} deleted.')

# Add commands to the CLI group
cli.add_command(add_author)
cli.add_command(list_authors)
cli.add_command(update_author)
cli.add_command(delete_author)
if __name__ == "__main__":
    cli()
    