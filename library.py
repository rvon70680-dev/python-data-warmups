import ollama

books = [
    {"title": "clean code", "author": "Robert Martin", "year": 2000, "pages": 255},
    {"title": "Python Crash Course", "author": "Eric Matthes", "year": 2019, "pages": 544},
    {"title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "year": 2017, "pages": 616},
    {"title": "The Pragmatic Programmer", "author": "Hunt and Thomas", "year": 1999, "pages": 352},
    {"title": "AI Engineering", "author": "Chip Huyen", "year": 2025, "pages": 532},
]

def describe(book):
    title = book["title"]
    author = book["author"]
    year = book["year"]
    page = book["pages"]

    return f"the title is {title} and it is published on {year} by {author} having {page} pages"


#for book in books:
#    print(describe(book))

def newer_than(books,year):
    result=[]
    for book in books:
        if book["year"] > year:
            result.append(book)
    return result   

for book in newer_than(books, 2010):
    print(describe(book))


def total_pages(books):
    total = 0
    for book in books:
        total += book["pages"]
    return total

print("Total pages:", total_pages(books))


############################ Ollama LLM Integration ##########################################

## Checking GPU usage for Ollama models cause of crash in some cases when the GPU is full
def show_gpu_usage():
    for m in ollama.ps().models:
        total = m.size
        on_gpu = m.size_vram
        percent = on_gpu / total * 100
        print(f"{m.model}: {on_gpu / 1e9:.1f} GB of {total / 1e9:.1f} GB on GPU ({percent:.0f}%)")


def print_llm_response(prompt):
    response = ollama.chat("llama3.1:8b", messages=[{"role": "user", "content": prompt}])
    print(response["message"]["content"])

def book_summary(book):
    prompt = f"Summarize the book '{book['title']}' by {book['author']} published in {book['year']}."
    print_llm_response(prompt)

print(book_summary(books[1]))  
show_gpu_usage()      