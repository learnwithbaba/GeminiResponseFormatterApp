def clean_html_text(raw_text: str) -> str:
    if not raw_text:
        return ""


    processed = raw_text.replace("\\n", "")
    processed = processed.replace('\\"', '"')
    return processed