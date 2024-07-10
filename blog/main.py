import re

def filter_text(name):
    # Function to extract URLs from text using regex
    def extract_urls(text):
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, text)
        return urls

    # File paths
    input_file = f'media/{name}'
    output_file = 'media/filter.txt'

    # Read from input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract URLs from the content
    urls = extract_urls(content)

    # Write URLs back to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')

    print(f'Extracted and saved {len(urls)} URLs to {output_file} successfully.')

