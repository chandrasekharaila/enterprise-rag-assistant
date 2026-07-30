from app.ingestion.loader_factory import LoaderFactory


loader = LoaderFactory.get_loader("data/sample.pdf")

document = loader.load()

print(document.content[:500])

print(document.metadata)