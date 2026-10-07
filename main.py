from loaders.document_loaders import(
    load_pdf,
    load_txt,
    load_docx,
    load_csv,
    load_youtube
)

def inspect_documents(documents):

    print("Number of Documents:", len(documents))

    for i, docuemnt in enumerate(documents):

        print(f"\n----Document {i}-----")

        print("Type:")
        print(type(docuemnt))

        print("\nPage Content:")
        print(docuemnt.page_content[:500])

        print("\nMetadata:")
        print(docuemnt.metadata)


def run_loader(name, loader_function, source):
    print("\n"+"="*60)
    print(name)
    print("="*60)

    try:
        documents = loader_function(source)

        print("Loader executed successfully!!")

        inspect_documents(documents)

    except Exception as e:

        print("Error while loading data.")
        print("Details:", e)


# PDF

run_loader(
    "PDF LOADER",
    load_pdf,
    "data/sample_pdf.pdf"
)

# TXT

run_loader(
    "TEXT LOADER",
    load_txt,
    "data/sample.txt"
)

# DOCX

run_loader(
    "DOCX LOADER",
    load_docx,
    "data/sample.docx"
)

# CSV

run_loader(
    "CSV LOADER",
    load_csv,
    "data/sample.csv"
)

# Youtube

youtube_url = "https://www.youtube.com/watch?v=phWxA89Dy94"

run_loader(
    "YOUTUBE LOADER",
    load_youtube,
    youtube_url
)