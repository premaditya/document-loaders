# LangChain Document Loaders

## Introduction

In this project, I worked with different Document Loaders in LangChain to understand how different types of raw data are converted into structured `Document` objects.

The five loaders used in this project are:

* PDF Loader
* Text Loader
* DOCX Loader
* CSV Loader
* YouTube Loader

The main thing I wanted to understand from this project is:

**How does different raw data become structured Documents that we can work with in a GenAI application?**

---

## Project Structure

```text
langchain_document_loaders/
│
├── data/
│   ├── sample_pdf.pdf
│   ├── sample.txt
│   ├── sample.docx
│   └── sample.csv
│
├── loaders/
│   └── document_loaders.py
│
├── main.py
│
└── README.md
```

---

# 1. PDF Loader

### Loader Used

```python
PyPDFLoader
```

### What I Loaded

I loaded a PDF file named:

```text
data/sample_pdf.pdf
```

### Output

The loader executed successfully and created:

```text
Number of Documents: 27
```

This means the PDF had 27 pages and the loader created one `Document` for each page.

The type of each output was:

```python
<class 'langchain_core.documents.base.Document'>
```

### Page Content

The `page_content` contains the text extracted from the PDF.

For example, the first Document contained address information such as:

```text
#205, 2nd Floor, Fortune
Signature, Near JNTU
Metro Station, Kukatpally,
Hyderabad, Telangana
500085
```

So, the actual text extracted from the PDF is stored inside `page_content`.

### Metadata

The metadata contained more information about the PDF.

Example:

```python
{
    'producer': 'Adobe PDF library 16.00',
    'creator': 'Adobe Illustrator 25.4 (Windows)',
    'creationdate': '2025-07-07T12:30:21+06:30',
    'author': 'MEENA DEGALA',
    'moddate': '2025-07-07T12:30:22+05:30',
    'title': 'PDF',
    'source': 'data/sample_pdf.pdf',
    'total_pages': 27,
    'page': 0,
    'page_label': '1'
}
```

From this I understood that PDF metadata can contain information like:

* Source
* Page number
* Total pages
* Author
* Title
* Creator
* Creation date

### My Observation

The important thing I observed from the PDF Loader is that **each page became a separate Document**.

So:

```text
27 PDF pages
        ↓
27 Documents
```

The `page_content` contains the text of that page and the metadata tells us information about the PDF and the page.

---

# 2. Text Loader

### Loader Used

```python
TextLoader
```

### What I Loaded

I loaded:

```text
data/sample.txt
```

### Output

The loader executed successfully and created:

```text
Number of Documents: 1
```

The output type was:

```python
<class 'langchain_core.documents.base.Document'>
```

### Page Content

The `page_content` contained the text from the text file.

For example:

```text
Artificial Intelligence is a branch of computer science that focuses
on creating systems capable of performing tasks that normally require
human intelligence.
```

The text continues with information about Artificial Intelligence and Machine Learning.

### Metadata

The metadata was:

```python
{'source': 'data/sample.txt'}
```

### My Observation

Unlike the PDF Loader, the Text Loader created only one Document for the complete text file.

So:

```text
1 TXT file
    ↓
1 Document
```

The actual text is stored in `page_content` and the source file information is stored in metadata.

---

# 3. DOCX Loader

### Loader Used

```python
Docx2txtLoader
```

### What I Loaded

I loaded:

```text
data/sample.docx
```

### Output

The loader executed successfully and created:

```text
Number of Documents: 1
```

The output type was:

```python
<class 'langchain_core.documents.base.Document'>
```

### Page Content

The `page_content` contained the text extracted from the Word document.

The document started with:

```text
Screenless Display: The Future of Visual Technology

Abstract

The rapid advancement of display technology has led to the emergence
of screenless displays...
```

### Metadata

The metadata was:

```python
{'source': 'data/sample.docx'}
```

### My Observation

The DOCX Loader extracted the text from the Word document and stored it inside `page_content`.

It created one Document for the DOCX file in my experiment.

So:

```text
1 DOCX file
      ↓
1 Document
```

The loader only extracts and structures the content. It does not understand the meaning of the document.

---

# 4. CSV Loader

### Loader Used

```python
CSVLoader
```

### What I Loaded

I loaded:

```text
data/sample.csv
```

The CSV contained movie-related information such as:

```text
movieId
title
genres
```

### Output

The loader executed successfully and created:

```text
Number of Documents: 13
```

### Page Content

The CSV data was converted into text inside `page_content`.

For example, one Document contained:

```text
: 0
Unnamed: 0.2: 0.0
Unnamed: 0.1: 0.0
Unnamed: 0: 0.0
movieId: 1
title: Toy Story (1995)
genres: ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy']
```

So the column names and their values are represented inside `page_content`.

### Metadata

For the first row, the metadata was:

```python
{'source': 'data/sample.csv', 'row': 0}
```

For the next row:

```python
{'source': 'data/sample.csv', 'row': 1}
```

and so on.

### My Observation

The important thing I observed from the CSV Loader is that **each row is converted into a separate Document**.

So:

```text
13 CSV rows
      ↓
13 Documents
```

The row number is also available in metadata.

One thing I noticed in my CSV is that it contains columns like:

```text
Unnamed: 0
Unnamed: 0.1
Unnamed: 0.2
```

These were also included in the `page_content`.

This shows that the data present in the CSV is directly represented when the loader creates the Documents.

---

# 5. YouTube Loader

### Loader Used

```python
YoutubeLoader
```

### What I Loaded

I used a YouTube video URL related to CSS Flexbox and Grid.

### Output

The loader executed successfully and created:

```text
Number of Documents: 1
```

The output type was:

```python
<class 'langchain_core.documents.base.Document'>
```

### Page Content

The transcript of the YouTube video was stored in `page_content`.

For example, the transcript started with information about how developers used floats and positioning before Flexbox was introduced.

So the video transcript becomes text that can be worked with like other Documents.

### Metadata

The metadata returned in my experiment was:

```python
{'source': 'phWxA89Dy94'}
```

Here the source represents the YouTube video ID.

### My Observation

The YouTube Loader converted the available video transcript into a Document.

So:

```text
YouTube Video
      ↓
Transcript
      ↓
1 Document
```

The transcript is stored in `page_content` and the video ID is stored in metadata.

---

# Loader Comparison

| Data Type | Loader           | Documents Created | `page_content`              | Metadata                                       |
| --------- | ---------------- | ----------------: | --------------------------- | ---------------------------------------------- |
| PDF       | `PyPDFLoader`    |                27 | Text from each PDF page     | Source, page, total pages, author, title, etc. |
| TXT       | `TextLoader`     |                 1 | Text from the TXT file      | Source                                         |
| DOCX      | `Docx2txtLoader` |                 1 | Text from the Word document | Source                                         |
| CSV       | `CSVLoader`      |                13 | Column names and row values | Source, row                                    |
| YouTube   | `YoutubeLoader`  |                 1 | Video transcript            | YouTube video ID                               |

---

# Understanding Document Object

After using all the loaders, I understood that the output from the loaders is not just plain text.

The loader creates a `Document` object.

A Document mainly contains:

```python
document.page_content
document.metadata
```

### `page_content`

This contains the actual extracted information.

For example:

* PDF → text from the page
* TXT → text from the file
* DOCX → text from the document
* CSV → row data
* YouTube → transcript

### `metadata`

This contains information about the source of the content.

For example:

* PDF → page number and source
* TXT → source file
* DOCX → source file
* CSV → source and row number
* YouTube → video ID

So I understood it as:

```text
page_content → What is the information?

metadata → Where did the information come from?
```

---

# Error Handling

I used `try-except` while loading the files.

Example:

```python
try:
    documents = loader.load()
    print("Loader executed successfully!!")

except Exception as e:
    print("Error while loading data.")
    print("Details:", e)
```

This helps to prevent the complete program from stopping when there is an error while loading a particular file.

For example, an error can happen because:

* File path is incorrect
* File does not exist
* CSV is not formatted properly
* YouTube transcript is not available
* Required package is missing

The error can then be displayed so that we can understand what went wrong.

---

# What I Understood From This Project

Before this project, different data formats looked like completely different types of data.

After using the loaders, I understood that LangChain converts these different data sources into a common structure called a `Document`.

The basic flow is:

```text
PDF
TXT
DOCX
CSV
YouTube
 │
 │
 ▼
Document Loader
 │
 ▼
Document
 ├── page_content
 └── metadata
```

The main difference between the loaders is how they divide and represent the original data.

For example:

```text
PDF
27 pages → 27 Documents

TXT
1 file → 1 Document

DOCX
1 file → 1 Document

CSV
13 rows → 13 Documents

YouTube
Transcript → 1 Document
```

This is useful in GenAI and RAG applications because after loading, the Documents can be further processed, split into chunks, converted into embeddings and stored in a vector database.

---

# Final Understanding

The main thing I understood from this project is that **Document Loaders are used to bring different types of raw data into a common Document format**.

The loader does not understand the meaning of the data.

It mainly does:

```text
Raw Data
   ↓
Document Loader
   ↓
Document
   ↓
page_content + metadata
```

After this, the Documents can be used for further steps in a GenAI or RAG application.