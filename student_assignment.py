from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

def load_with_PyPdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs


def hw02_1(q1_pdf):
    docs = load_with_PyPdf(q1_pdf)
    print("doc("+ q1_pdf +") has " + str(len(docs)) + " page(s)")
    last_page_index = len(docs) - 1
    #print(docs[last_page_index])
    return docs[last_page_index]
    
def hw02_2(q2_pdf):
    docs = load_with_PyPdf(q2_pdf)
    text = ""
    for doc in docs:
        text = text + doc.page_content + "\n"

    spliter = RecursiveCharacterTextSplitter(separators=["第 .* 章 .*\n","第 \\d+-?\\d* 條\n"],
                                    chunk_size=0,
                                    chunk_overlap=0,
                                    is_separator_regex=True,
                                    keep_separator=True)
    result = spliter.create_documents([text])
    #print(len(result))
    return len(result)

if __name__ == "__main__":
    #hw02_1(q1_pdf)
    #hw02_2(q2_pdf)